# Naija Farmers Northstar — ADTC 2026 Submission Report

## Problem
Nigerian smallholder groundnut farmers in the Sudan and Guinea savanna zones lack access to reliable agricultural advisory services. Extension officers are understaffed, internet connectivity is unreliable, and existing digital tools require cloud access. This system provides offline, on-device agronomic advice sourced from peer-reviewed Nigerian extension documents.

## Target User
Smallholder groundnut farmers in northern Nigeria, specifically Kano, Kaduna, Katsina, and Jigawa states — the core of Nigeria's historic groundnut belt.

## Design Decisions
- **Model:** Phi-3 Mini 3.82B at Q4_K_M quantization. Chosen for balance between reasoning quality and RAM footprint (~2.3GB loaded), leaving headroom for RAG and OS overhead within the 8GB constraint.
- **Runtime:** llama.cpp — required by competition rules, compiled from source on Ubuntu 22.04.
- **RAG:** LlamaIndex with BAAI/bge-small-en-v1.5 local embeddings. Index built from ICRISAT/IAR/FMARD groundnut extension documents. No internet required at inference time.
- **Corpus:** Primary source is A Farmers Guide to Profitable Groundnut Production in Nigeria (ICRISAT + IAR Ahmadu Bello University Zaria + FMARD, 2015). Selected because it is the definitive Nigerian groundnut extension document co-authored by IAR Zaria — the research institute on the same campus as my university.

## Constraints
- Hardware: 8GB RAM, 4 vCPU, integrated GPU, Ubuntu 22.04
- Zero network calls during inference
- All embeddings and model weights loaded locally

## Benchmarks
- Prompt processing: ~9 t/s
- Token generation: ~4.5 t/s
- Peak RAM: ~3.2GB
- Thermal: no throttling observed

## African Use Case Claim
This system targets Nigerian smallholder groundnut farmers — the demographic that built the Kano groundnut pyramids and still represents the majority of northern Nigeria agricultural workforce. The RAG corpus is sourced directly from Nigerian government and ICRISAT Nigeria publications. The developer is an agriculture student at Ahmadu Bello University Zaria with direct farmer network access for ground-truth validation.
