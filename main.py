alphabet = 'abcdefghijklmnopqrstuvwxyz' # I will re-arrange the alphabet
shift = 5 # This will be the new starting index, (f)

# Slice the alphabet starting at the index stored in 'shift' through the end,
# then concatenate the slice from the start of the alphabet up to 'shift' to rotate it.
shifted_alphabet = alphabet[shift:] + alphabet[:shift] 