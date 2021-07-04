# Config System

## Heading 1

[config]  
deck_name = "Export2"  
tags = ["test1","test2"]

Q.  
A.

[inlineconfig]  
tags = ["inline","config"]  
[/inlineconfig]  
Inline config is possible.  
This would only affect the current block.

Q2.  
A2.

## Heading 2

The config will only affect the blocks under it having the same ancestor.  
That's implemented by a Depth-First Search.

[config]  
tags = ["test3","test4"]

Overriding is **possible**.

A multiple Card **test**.

### Sub Heading 3

And cards here would be affected too.  
Hmm.

[inlineconfig]  
skip = true  
[/inlineconfig]  
skip this block!

[inlineconfig]  
skip = true  
[/inlineconfig]  
please use lowercase.

[config]  
skip = true

You can skip a lot of things...  

Write something you like.  

And when we exit this heading, the config will be reverted.

## Heading 4

[config]  
tags = ["test5"]

Old time returns.  
Here we are.

[inlineconfig]  
mathjax = false  
[/inlineconfig]  
$100 free of **mathjax**!

#THIS won't be recognized as a heading when being parsed.
interesting right? Avoid this improper syntax.

[config]
[notetype.Cloze]
clozePrefix = "\\("
clozeSuffix = "\\)"
clozeNumberPrefix = "\\{"
clozeNumberSuffix = "\\}"

Special (Cloze) and ({1}Numbering).
