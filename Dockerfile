FROM python:3.9-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install dependencies in a separate layer
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install watchdog

# Use a multi-stage build for a smaller image
FROM python:3.9-slim

WORKDIR /app

# Create a non-root user for security
RUN groupadd -g 1000 streamlit && \
    useradd -u 1000 -g streamlit -s /bin/bash -m streamlit && \
    chown -R streamlit:streamlit /app

# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application files
COPY --chown=streamlit:streamlit . .

# Make directories required for file upload functionality
RUN mkdir -p /app/uploads && chown -R streamlit:streamlit /app/uploads

# Switch to non-root user
USER streamlit

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8501/ || exit 1

# Set application entry point
CMD ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0", "app.py"]
