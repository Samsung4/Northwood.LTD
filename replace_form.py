#!/usr/bin/env python3
import os
import re

# this regex will match the opening <form> tag that has id="wf-form-Contact-Form"
FORM_PATTERN = re.compile(
    r'<form\b[^>]*\bid="wf-form-Contact-Form"[^>]*>',
    re.IGNORECASE | re.DOTALL
)

# the replacement Formspree form tag
REPLACEMENT = '''<form id="wf-form-Contact-Form"
      name="wf-form-Contact-Form"
      data-name="Contact Form"
      action="https://formspree.io/f/xdkevwzl"
      method="POST"
      class="form-2">'''

def replace_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    new_text, count = FORM_PATTERN.subn(REPLACEMENT, text)
    if count:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_text)
    return count

def main():
    total = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for fn in filenames:
            if fn.lower().endswith(('.html', '.htm')):
                full = os.path.join(dirpath, fn)
                n = replace_in_file(full)
                if n:
                    print(f"[{n:2d}] replacements in {full}")
                    total += n
    print(f"\nDone — total replacements: {total}")

if __name__ == '__main__':
    main()
