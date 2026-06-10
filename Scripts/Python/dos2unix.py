import sys

# This script converts a file from DOS format (CRLF) to Unix format (LF).
def dos2unixpy(input_file, output_file=None):
    """Read input_file, replace CRLF with LF, write to output_file or stdout."""
    with open(input_file, "rb") as rf:
        raw = rf.read()

    # Replace CRLF with LF (binary mode to handle exact bytes)
    data = raw.replace(b"\r\n", b"\n")

    if output_file:
        with open(output_file, "wb") as wf:
            wf.write(data)
    else:
        sys.stdout.buffer.write(data)

if __name__ == "__main__":
    dos2unixpy("a.py", "b.py")