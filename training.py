# nvidia-smi

# https://github.com/zeke-john/WaysteAI.git

# cd WaysteAI

# pip3 install torch==1.8.1+cu111 -f

# pip install wandb pydu

#python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft

# python3 musicgenTrainer/run.py --dataset_path output


#ERROR

# /opt/conda/lib/python3.10/site-packages/audiocraft/models/musicgen.py:127: UserWarning: MusicGen pretrained model relying on deprecated checkpoint mapping. Please use full pre-trained id instead: facebook/musicgen-large
#   warnings.warn(
# /opt/conda/lib/python3.10/site-packages/torch/nn/utils/weight_norm.py:30: UserWarning: torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.
#   warnings.warn("torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.")
# Tuning everything
# Traceback (most recent call last):
#   File "/home/ubuntu/WaysteAI/WaysteAI/musicgenTrainer/run.py", line 21, in <module>
#     train(
#   File "/home/ubuntu/WaysteAI/WaysteAI/musicgenTrainer/train.py", line 200, in train
#     lm_output = model.lm.compute_predictions(
#   File "/opt/conda/lib/python3.10/site-packages/audiocraft/models/lm.py", line 297, in compute_predictions
#     logits = model(sequence_codes, conditions, condition_tensors)  # [B, K, S, card]
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
#     return self._call_impl(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
#     return forward_call(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/audiocraft/models/lm.py", line 253, in forward
#     out = self.transformer(input_, cross_attention_src=cross_attention_input)
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
#     return self._call_impl(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
#     return forward_call(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/audiocraft/modules/transformer.py", line 698, in forward
#     x = self._apply_layer(layer, x, *args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/audiocraft/modules/transformer.py", line 655, in _apply_layer
#     return layer(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
#     return self._call_impl(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
#     return forward_call(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/audiocraft/modules/transformer.py", line 550, in forward
#     self._sa_block(self.norm1(x), src_mask, src_key_padding_mask))
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/transformer.py", line 715, in _sa_block
#     x = self.self_attn(x, x, x,
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
#     return self._call_impl(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
#     return forward_call(*args, **kwargs)
#   File "/opt/conda/lib/python3.10/site-packages/audiocraft/modules/transformer.py", line 365, in forward
#     projected = nn.functional.linear(query, self.in_proj_weight, self.in_proj_bias)
# torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 72.00 MiB. GPU 0 has a total capacty of 14.58 GiB of which 27.56 MiB is free. Including non-PyTorch memory, this process has 14.55 GiB memory in use. Of the allocated memory 13.75 GiB is allocated by PyTorch, and 682.30 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF