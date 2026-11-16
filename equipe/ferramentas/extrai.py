import pdfplumber,sys,json
F='/home/claude/fontes/'
def extrai(pdfname,out):
    pdf=pdfplumber.open(F+pdfname); pages=[]; struck_total=0; tot=0
    for p in pdf.pages:
        thin=[r for r in (p.rects+p.lines) if (r['bottom']-r['top'])<1.6 and (r['x1']-r['x0'])>3]
        def keep(o):
            if o['object_type']!='char': return True
            mid=(o['top']+o['bottom'])/2; h=o['bottom']-o['top']; cx=(o['x0']+o['x1'])/2
            for r in thin:
                ry=(r['top']+r['bottom'])/2
                if r['x0']-0.5<=cx<=r['x1']+0.5 and abs(ry-mid)<=h*0.22: return False
            return True
        n0=len(p.chars); q=p.filter(keep); n1=len(q.chars); struck_total+=n0-n1; tot+=n0
        pages.append(q.extract_text(x_tolerance=1.5,y_tolerance=3) or '')
    open(F+out,'w',encoding='utf-8').write('\n'.join(pages))
    print(pdfname,'chars',tot,'riscados',struck_total)
extrai('cristalina-lei-1207-1994.pdf','est.clean.txt')
extrai('cristalina-lei-organica-consolidada.pdf','lo.clean.txt')
extrai('cristalina-regimento-interno-2026.pdf','ri.clean.txt')
