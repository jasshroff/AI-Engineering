# import sys
# import shutil
# import subprocess

# CHECKS = [
#     ("Python 3.10+", lambda: sys.version_info >= (3, 10), f"Python {sys.version}"),
#     ("NumPy", lambda: __import__("numpy"), None),
#     ("Matplotlib", lambda: __import__("matplotlib"), None),
#     ("Jupyter", lambda: __import__("jupyter"), None),
#     ("Git", lambda: shutil.which("git") is not None, None),
#     ("Node.js", lambda: shutil.which("node") is not None, None),
#     ("Rust (cargo)", lambda: shutil.which("cargo") is not None, None),
# ]

# GPU_CHECKS = [
#     ("PyTorch", lambda: __import__("torch"), None),
#     (
#         "CUDA",
#         lambda: __import__("torch").cuda.is_available(),
#         lambda: __import__("torch").cuda.get_device_name(0) if __import__("torch").cuda.is_available() else "Not available",
#     ),
# ]


# def run_check(name, check_fn, detail_fn=None):
#     try:
#         result = check_fn()
#         if result is False:
#             raise Exception("Check returned False")
#         detail = ""
#         if detail_fn:
#             if callable(detail_fn):
#                 detail = f" ({detail_fn()})"
#             else:
#                 detail = f" ({detail_fn})"
#         print(f"  [PASS] {name}{detail}")
#         return True
#     except Exception:
#         print(f"  [FAIL] {name}")
#         return False


# def main():
#     print("\n=== AI Engineering from Scratch — Environment Check ===\n")

#     print("Core:")
#     passed = sum(run_check(name, fn, detail) for name, fn, detail in CHECKS)
#     total = len(CHECKS)

#     print("\nGPU (optional):")
#     gpu_passed = sum(run_check(name, fn, detail) for name, fn, detail in GPU_CHECKS)
#     gpu_total = len(GPU_CHECKS)

#     print(f"\nResult: {passed}/{total} core checks passed", end="")
#     if gpu_passed > 0:
#         print(f", {gpu_passed}/{gpu_total} GPU checks passed")
#     else:
#         print(" (no GPU — that's fine, most lessons work on CPU)")

#     if passed == total:
#         print("\nYou're ready. Start with Phase 1.\n")
#     else:
#         print("\nFix the failed checks above, then run this script again.\n")

#     return 0 if passed == total else 1


# if __name__ == "__main__":
#     sys.exit(main())



# import torch
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print(f"Using: {device}")


import torch
import time

size = 5000

a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU: {gpu_time:.3f}s")
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")