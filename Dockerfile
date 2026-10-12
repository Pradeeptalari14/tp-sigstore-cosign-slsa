FROM python:3.11-slim as builder
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pyyaml requests || true

FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app
COPY --from=builder /app /app
USER 65532:65532
ENTRYPOINT ["python", "scripts/validate.sh"]
