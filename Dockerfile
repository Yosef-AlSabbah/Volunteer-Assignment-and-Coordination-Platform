# Use an official Python runtime as a parent image
FROM python:3.13.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv
# This ensures uvicorn and all other dependencies are properly installed
RUN uv pip install --system .

# Copy the rest of the application code
COPY . .

# Expose port 8000 for the Django app
EXPOSE 8000

# The actual command will be overridden by docker-compose.yml
# This is a fallback command if running the container directly
CMD ["uvicorn", "volunteer_platform.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
