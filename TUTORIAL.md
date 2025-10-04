```bash
filtool -v --filplan /data/filplan.json -f /data/frb.fil -o /data/frb.cleaned.fil
```

```bash
transientx_fil \
  -v \
  -t 4 \
  --zapthre 3.0 \
  --fd 1 \
  --overlap 0.1 \
  --ddplan /data/ddplan.txt \
  --thre 7 \
  --maxw 0.1 \
  --snrloss 0.1 \
  -l 2.0 \
  --drop \
  -z kadaneF 8 4 zdot \
  -f /data/frb.cleaned.fil
```
