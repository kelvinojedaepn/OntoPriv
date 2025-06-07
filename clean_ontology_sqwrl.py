import re  # Regular expressions module for text pattern matching

# Input and output file paths
input_file = r"input_file.owx"          # Original ontology file containing SQWRL rules
output_file = r"cleaned_ontology.owl"   # Output file after removing SQWRL rules

# Read the full content of the input ontology file as plain text
with open(input_file, "r", encoding="utf-8") as f:
    file_content = f.read()

# Define the regex pattern to remove SQWRL-based SWRL rules
# Pattern breakdown:
# <DLSafeRule>                   → Match the start of a SWRL rule block
# .*?                            → Non-greedy match of any content until the next part
# <BuiltInAtom[^>]*sqwrl[^>]*>   → Match a BuiltInAtom tag that contains the string "sqwrl"
#                                  - [^>]* means any character except '>', zero or more times
#                                  - ensures we scan all attributes to find "sqwrl"
# .*?                            → Continue matching anything after the BuiltInAtom, non-greedy
# </DLSafeRule>                  → Match the end of the SWRL rule block
# Result: Entire <DLSafeRule>...</DLSafeRule> block is removed only if it contains a SQWRL atom
cleaned_content = re.sub(
    r"<DLSafeRule>.*?<BuiltInAtom[^>]*sqwrl[^>]*>.*?</DLSafeRule>",
    "",                  # Replace matched SQWRL rule block with an empty string (i.e., delete it)
    file_content,        # Apply regex substitution to the entire ontology content
    flags=re.DOTALL      # Makes '.' match newline characters as well (enables multi-line matching)
)

# Write the cleaned ontology (without SQWRL rules) to a new file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(cleaned_content)

print("ok", output_file)  # Confirmation that the cleaned file was written successfully