# Simple Net Mask translation

Argv is handled first and then, piped input will be handled.

### Awereness
- `mask.{py,sh}` must be on the same folder
- requirements for `mask.sh`:
>* `ifconfig`
>* `grep`
>* `awk`


### Usage
```./mask.sh```  will show all masks translation (execption of localhost) given by `ifconfig`
