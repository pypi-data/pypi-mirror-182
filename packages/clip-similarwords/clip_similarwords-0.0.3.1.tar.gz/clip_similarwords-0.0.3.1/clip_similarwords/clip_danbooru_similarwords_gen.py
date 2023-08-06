
# Copyright 2022 Toshimitsu Kimura <lovesyao@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# worked on RTX 3060 VRAM 12GB
import torch
import transformers
import time
from tqdm import tqdm
import os, sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

class CLIPTextSimilarWordsGen(transformers.CLIPTextModel):
    def __init__(self, config: transformers.CLIPTextConfig):
        super().__init__(config)

    @torch.no_grad()
    def forward(self, variant_prompts, non_padding_length, dan_tensor, dan_non_padding_length):
        similarities = torch.empty(0, dtype=torch.half, device="cuda")#torch.cuda.HalfTensor()
        idx = torch.empty(0, dtype=torch.int64, device="cuda")
        tokens = torch.full((64, 77), 49407, dtype=torch.int64, device="cuda")
        tokens[:, 0] = 49406
        variant_embeddings = torch.empty((variant_prompts.shape[0], 77*768), dtype=torch.half, device="cuda")

        for i in tqdm(range(0, variant_prompts.shape[0], 64)):
            tokens[:, 1] = variant_prompts[i:i+64]
            variant_embeddings[i:i+64] = super().forward(tokens)[0].flatten(1)

        dan_embeddings = torch.empty((dan_tensor.shape[0], 77*768), dtype=torch.half, device="cuda")
        for i in tqdm(range(0, dan_tensor.shape[0], 64)):
            dan_embeddings[i:i+64] = super().forward(dan_tensor.cuda()[i:i+64])[0].flatten(1)

#        print(variant_embeddings.shape)
        variant_embeddings = variant_embeddings[0:non_padding_length]
        dan_embeddings = dan_embeddings[0:dan_non_padding_length]

        variant_embeddings_norm = torch.linalg.norm(variant_embeddings, dim=1, keepdim=True)
        variant_embeddings /= variant_embeddings_norm
        del variant_embeddings_norm
        dan_embeddings_norm = torch.linalg.norm(dan_embeddings, dim=1, keepdim=True)
        dan_embeddings /= dan_embeddings_norm
        del dan_embeddings_norm
#        print(variant_embeddings_norm.shape)
#        print(variant_embeddings_norm2.shape)

        t = torch.matmul(variant_embeddings, dan_embeddings.T)
#        print(y.shape)
        del variant_embeddings
        del dan_embeddings

        mask = t >= 0.85
#        mask2 = t != 1.0
#        mask &= mask2
        nz = torch.nonzero(mask)
#        print(nz.shape)
        print(t[mask].shape) # 閾値 0.85 で torch.Size([43304])
        return (nz, t[mask])

if __name__ == '__main__':
    model_path = "/home/nazo/.cache/huggingface/diffusers/models--CompVis--stable-diffusion-v1-4____/snapshots/a304b1ab1b59dd6c3ba9c40705c29c6de4144096/"
    #model_path = "/home/nazo/.cache/huggingface/diffusers/Anything-V3.0/"
    model_path += "text_encoder/"

    tokenizer = transformers.CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
    arr = [sk for sk, s in tokenizer.decoder.items() if s[-4:] == "</w>"]
    #arr = [sk for sk, s in tokenizer.decoder.items() if s == "kitty</w>"]
    non_padding_length = len(arr)
    if len(arr) % 64 != 0:
        arr += [49407] * (64 - (len(arr) % 64)) # padding
    assert(len(arr) % 64 == 0)
    variant_prompts = torch.cuda.LongTensor(arr)

    import pickle
    dan_tags = pickle.load(open(parent_dir + "/../tmp_danbooru_tags.pt", "rb"))
    dan_non_padding_length = len(dan_tags)
    if len(dan_tags) % 64 != 0:
        dan_tags += [""] * (64 - (len(dan_tags) % 64)) # padding
    assert(len(dan_tags) % 64 == 0)
    dan_tensor = tokenizer(dan_tags, padding="max_length", max_length=77, return_attention_mask=False, return_tensors="pt").input_ids

    f = CLIPTextSimilarWordsGen.from_pretrained(model_path).to("cuda").half()
    idx, similarities = f(variant_prompts, non_padding_length, dan_tensor, dan_non_padding_length)
#    print(idx[:,1][idx[:,1] >= 9176])
    idx[:,0] = variant_prompts[idx[:,0]]
#    torch.save((idx, similarities), "clip_similarwords.pt")

    out_dict = {}
    for i, k in enumerate(idx):
         key = int(k[1])
         if key not in  out_dict:
             out_dict[key] = []
         out_dict[key] += [(int(k[0]), float(similarities[i]))]

#    torch.save(out_dict, "clip_similarwords_dict.pt")

#    with open("clip_similarwords_dict.pt", "wb") as f:
#        pickle.dump(out_dict, f)

    with open("clip_danbooru_similarwords_all.pt", "wb") as f: # transformers is slow on startup and causes warnings so we just include its decoder
        pickle.dump((tokenizer.decoder, dan_tags, out_dict), f)

#    print(idx)
#    print(similarities)

#    similarities = similarities.detach().cpu().numpy()
#    variant_prompts = variant_prompts.detach().cpu().numpy()
#
#    import regex as re
#    for i, k in enumerate(idx):
#         print("%s :: %s :: cossim: %.2f"%(tokenizer.decoder[variant_prompts[k[0]]].replace("</w>", ""), tokenizer.decoder[variant_prompts[k[1]]].replace("</w>", ""), similarities[i]))

