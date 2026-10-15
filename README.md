<p align="center">
  <img src="https://raw.githubusercontent.com/LeslieWylie/LeslieWylie/main/assets/header.svg" alt="Lele — Agent Engineering &amp; Inference Systems" width="100%" />
</p>

# Hi, I'm Lele

I build tools that help AI agents remember, collaborate, and show their evidence. I also work on practical inference systems, with a focus on multimodal and video generation.

我关注 **Agent 工程与模型推理优化**：让智能体有可追溯的记忆、清晰的协作流程，让模型推理更高效、更可靠。

[Agent projects](#agent-projects) · [Open-source contributions](#open-source-contributions) · [More work](#more-work)

## What I work on

- **Agent memory** — source-backed retrieval, persistent context, and MCP integrations.
- **Agent workflows** — session search, structured review, and evidence-based evaluation.
- **Inference systems** — MiniMax H3 integration, video generation, LoRA correctness, and runtime fixes.

## Agent projects

| Project | What it does |
| :--- | :--- |
| **[repository-memory](https://github.com/LeslieWylie/repository-memory)** | Source-backed memory for coding agents, with Git citations, a local store, CLI, and MCP server. |
| **[dsh-ops-kit](https://github.com/LeslieWylie/dsh-ops-kit)** | Evidence-driven memory, orchestration, benchmark checks, and release workflows for DeepSeek Harness. |
| **[dsh-session-search-pro](https://github.com/LeslieWylie/dsh-session-search-pro)** | Search past and live DeepSeek Harness sessions through the runtime's own session service. |
| **[review-workflow](https://github.com/LeslieWylie/review-workflow)** | Structured review with independent panelists, disagreement resolution, and a separate critic. |

## Open-source contributions

A few merged contributions to upstream inference projects:

- **[FastVideo](https://github.com/hao-ai-lab/FastVideo)** — MiniMax H3 NVFP4-AWQ text encoder support ([#1865](https://github.com/hao-ai-lab/FastVideo/pull/1865)); preserve video frames when audio is shorter ([#1857](https://github.com/hao-ai-lab/FastVideo/pull/1857)); frame padding at the 15-second limit ([#1842](https://github.com/hao-ai-lab/FastVideo/pull/1842)).
- **[vLLM-Omni](https://github.com/vllm-project/vllm-omni)** — preserve CUDA toolkit header precedence in all-to-all JIT builds ([#7599](https://github.com/vllm-project/vllm-omni/pull/7599)).

Other proposals and discussions: [H3 8-NFE acceleration](https://github.com/vllm-project/vllm-omni/pull/7425) · [H3 final-layer fusion](https://github.com/vllm-project/vllm-omni/pull/8677) · [retryable LoRA activation](https://github.com/vllm-project/vllm/pull/61618).

[Browse all public pull requests →](https://github.com/pulls?q=is%3Apr+author%3ALeslieWylie+is%3Apublic)

## More work

- **[Coding-agent benchmark](https://github.com/LeslieWylie/terminal-bench-rl-novita-benchmark)** — a fixed-base software engineering task with a reference solution and an isolated verifier.
- **[Verifiable distributed inference](https://github.com/LeslieWylie/Distributed_inference_system_under_ZKP)** — an experimental framework using EZKL proofs to verify inference across model slices and workers.

**Tools I use:** Python · TypeScript / JavaScript · PyTorch · MCP · FastAPI · Docker

---

Based in Beijing · WeChat: **yaole516**
