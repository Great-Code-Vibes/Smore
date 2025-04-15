FROM nvidia/cuda:12.1.0-base-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip python3-dev \
    git wget \
    libgl1-mesa-glx libglib2.0-0 \
    build-essential \
    ocl-icd-opencl-dev opencl-headers clinfo \
    libffi-dev \
    libssl-dev \
    tk-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY smore/requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application
COPY . /app/

# Create necessary directories
RUN mkdir -p /app/smore/logs

# Create a non-root user
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Run the application
ENTRYPOINT ["python3", "-m", "smore.run_local"] 