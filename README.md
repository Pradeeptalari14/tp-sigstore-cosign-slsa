# Sigstore Cosign SLSA Provenance Studio

> **Production Repository:** `Pradeeptalari14/tp-sigstore-cosign-slsa`  
> **Interactive Studio Workspace:** [https://talaripradeep.info/tools/sigstore-cosign-slsa/](https://talaripradeep.info/tools/sigstore-cosign-slsa/)  
> **Visual Flow Canvas:** [https://talaripradeep.info/studios/flow/?studio=sigstore-cosign-slsa](https://talaripradeep.info/studios/flow/?studio=sigstore-cosign-slsa)

## Overview
Automate SLSA Level 3 build provenance, in-toto cryptographic attestations, and keyless container image signing using GitHub Actions OIDC and Rekor transparency log.

## Primary Specification Manifest: `cosign-attestation.yml`
```yaml
apiVersion: v1
kind: SigstoreCosignPipeline
metadata:
  name: sigstore-cosign-slsa
spec:
  oidcProvider: "https://token.actions.githubusercontent.com"
  rekorTransparencyUrl: "https://rekor.sigstore.dev"
  fulcioCertificateAuthority: "https://fulcio.sigstore.dev"
  slsaProvenanceLevel: 3
  signKeyless: true
  attestationPredicate: "https://slsa.dev/provenance/v1"
```

## Verification & Execution
```bash
# Run local verification
git verify-commit HEAD
```

## License
MIT License. Copyright (c) 2026 Talari Pradeep.
