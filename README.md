<p align="center">
  <img src="https://raw.githubusercontent.com/LeslieWylie/LeslieWylie/main/assets/header.svg" alt="Lele — Agent Engineering &amp; Inference Systems" width="100%" />
</p>

# Lele · Open-source contributor

I contribute to inference runtimes and agent tooling, focusing on multimodal generation, LoRA correctness, and agent memory.

我关注 **Agent 工程与模型推理优化**，通过上游 PR 贡献模型接入、推理优化和运行时修复。

[Merged PRs](#merged-prs) · [Open PRs](#open-prs) · [Agent projects](#agent-projects) · [All upstream PRs ↗](https://github.com/pulls?q=is%3Apr+author%3ALeslieWylie+is%3Apublic+-user%3ALeslieWylie)

## Merged PRs

| Project | Contribution | PR |
| :--- | :--- | :--- |
| **FastVideo** | Import MiniMax H3 Comfy NVFP4-AWQ text encoder weights. | [#1865](https://github.com/hao-ai-lab/FastVideo/pull/1865) |
| **vLLM-Omni** | Preserve CUDA toolkit header precedence in all-to-all JIT builds. | [#7599](https://github.com/vllm-project/vllm-omni/pull/7599) |
| **FastVideo** | Preserve video frames when decoded audio is shorter. | [#1857](https://github.com/hao-ai-lab/FastVideo/pull/1857) |
| **FastVideo** | Allow MiniMax H3 frame padding at the 15-second limit. | [#1842](https://github.com/hao-ai-lab/FastVideo/pull/1842) |

[All merged upstream PRs →](https://github.com/pulls?q=is%3Apr+author%3ALeslieWylie+is%3Apublic+is%3Amerged+-user%3ALeslieWylie)

## Open PRs

Selected proposals, open as of **2026-10-15**. Each PR links to its implementation, validation, and latest review status.

| Project | Proposed change | PR |
| :--- | :--- | :--- |
| **vLLM** | Keep failed LoRA activations retryable, avoiding a false active state after loading errors. | [#61618](https://github.com/vllm-project/vllm/pull/61618) |
| **vLLM** | Reject inconsistent LoRA checkpoint factor ranks and incomplete A/B pairs. | [#61605](https://github.com/vllm-project/vllm/pull/61605) |
| **vLLM** | Account for CLIP CLS rows in LLaVA tower-LoRA buffers and image mappings. | [#61799](https://github.com/vllm-project/vllm/pull/61799) |
| **vLLM-Omni** | Add task-scoped MiniMax H3 PDD acceleration with eight denoising evaluations. | [#7425](https://github.com/vllm-project/vllm-omni/pull/7425) |
| **vLLM-Omni** | Fuse H3 final affine and FP32 promotion while preserving input-dtype rounding. | [#8677](https://github.com/vllm-project/vllm-omni/pull/8677) |
| **SGLang** | Keep adaptive speculative-decoding target graph construction outside draft contexts. | [#40962](https://github.com/sgl-project/sglang/pull/40962) |
| **Memmy Agent** | Add dedicated SGLang/vLLM thinking-mode transports for memory LLM providers. | [#348](https://github.com/MemTensor/memmy-agent/pull/348) |
| **OpenVDN** | Add a persistent Ulysses request worker with optional low-memory decoding. | [#3](https://github.com/OpenVDN/vdn-minimax-h3/pull/3) |

[All open upstream PRs →](https://github.com/pulls?q=is%3Apr+author%3ALeslieWylie+is%3Apublic+is%3Aopen+-user%3ALeslieWylie)

## Agent projects

| Project | What it does |
| :--- | :--- |
| **[repository-memory](https://github.com/LeslieWylie/repository-memory)** | Source-backed memory for coding agents, with Git citations, a local store, CLI, and MCP server. |
| **[dsh-ops-kit](https://github.com/LeslieWylie/dsh-ops-kit)** | Evidence-driven memory, orchestration, benchmark checks, and release workflows for DeepSeek Harness. |
| **[dsh-session-search-pro](https://github.com/LeslieWylie/dsh-session-search-pro)** | Search past and live DeepSeek Harness sessions through the runtime's own session service. |
| **[review-workflow](https://github.com/LeslieWylie/review-workflow)** | Structured review with independent panelists, disagreement resolution, and a separate critic. |

Also exploring [coding-agent evaluation](https://github.com/LeslieWylie/terminal-bench-rl-novita-benchmark) and [verifiable distributed inference](https://github.com/LeslieWylie/Distributed_inference_system_under_ZKP).

**Tools I use:** Python · TypeScript / JavaScript · PyTorch · MCP · FastAPI · Docker

---

Based in Beijing · WeChat: **yaole516**
