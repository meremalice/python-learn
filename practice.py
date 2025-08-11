raw = "  drAKE  "
clean = raw.strip().title()          # "Drake"
slug  = clean.lower().replace(" ", "-")  # "drake"
line  = f"{clean:<10} | albums: {12:>3} | streams: {1_234_567:>12,}"
print(clean, slug, line, sep="\n")
