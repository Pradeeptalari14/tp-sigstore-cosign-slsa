#!/usr/bin/env python3
"""
Sigstore Cosign SLSA Provenance Signer & Verifier
Validates keyless OIDC container signatures against Rekor transparency log.
"""
import subprocess
import json
import sys

def verify_image_signature(image_ref: str, cert_identity: str, oidc_issuer: str) -> bool:
    cmd = [
        "cosign", "verify",
        "--certificate-identity-regexp", cert_identity,
        "--certificate-oidc-issuer", oidc_issuer,
        image_ref
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Verified {image_ref} against Rekor log.")
        return True
    else:
        print(f"❌ Verification failed: {result.stderr}", file=sys.stderr)
        return False

if __name__ == "__main__":
    verify_image_signature("ghcr.io/pradeep/app:sha-latest", ".*@github\.com", "https://token.actions.githubusercontent.com")
