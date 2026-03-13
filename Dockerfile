# Use the official Qdrant image as base
FROM qdrant/qdrant:latest

# Expose Qdrant ports
EXPOSE 6333 6334

# Optional: set working directory inside container
WORKDIR /qdrant

# Start Qdrant server
CMD ["./qdrant"]
