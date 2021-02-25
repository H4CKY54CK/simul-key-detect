# simul-key-detect
It uses state-of-the-art¹ key detection technology

¹ Reading from /dev/input

Detect simultaneous multiple key states

## Brief
Basically, all we're doing is reading `/dev/input/eventX`, where `X` is whichever file it is. There's something like 20-25 of them?

Since the owner of the files are `root:input`, we either need to run this python script as `sudo`, or add ourself to the `input` group (giving our python script access to the files).

We get the data as (TIME INTEGER, something, TIME DECIMAL, something, EVENT TYPE, KEY CODE, KEY STATE). We currently only care about the last 3.

EVENT TYPES that we are interested in are EVENT TYPE 1. If it's not, discard.

- If you only care about the keys, then just get the values of `self.keys[str(key_code)]['name']` and `self.keys[str(key_code)]['state']`. That's it.

To render the ASCII art keyboard, we set the current KEY STATE of the KEY CODE in a dict accessible within the class we created (already set up in the module), and we color the different keys as necessary.

Then print the keyboard.

That's literally it.

## Setup
Setup is actually kind of a bit of work. I'll try and remember my steps as best as I can. And I'll update this section soon, I promise.

####Basic Setup
Use `evtest` to get the list of keycodes and what character they are mapped to. `ls -l /dev/input/by-id` to find out which file your keyboard is talking to. Add yourself to the group that the file belongs to (in my case, this was `input`. I don't know if that's universal or not). ???. Python.
