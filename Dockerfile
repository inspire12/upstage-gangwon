FROM python:3.12-slim

WORKDIR /app

# Install uv via pip
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --no-cache

# Copy application code
COPY . .

# Expose port
EXPOSE 8800

# Run the application
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8800"]