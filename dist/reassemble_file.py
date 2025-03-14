def reassemble_file(output_file, chunk_prefix):
    """
    Reassembles a file from smaller chunks.

    :param output_file: Path to the output file.
    :param chunk_prefix: Prefix of the chunk files (e.g., "dist/main.exe.part").
    """
    part_num = 1
    with open(output_file, "wb") as f:
        while True:
            chunk_file = f"{chunk_prefix}{part_num}"
            try:
                with open(chunk_file, "rb") as part:
                    f.write(part.read())
                print(f"Added chunk: {chunk_file}")
                part_num += 1
            except FileNotFoundError:
                print("All chunks have been reassembled.")
                break

if __name__ == "__main__":
    
    output_file = "dist/main_reassembled.exe"
    chunk_prefix = "dist/main.exe.part"
    reassemble_file(output_file, chunk_prefix)


