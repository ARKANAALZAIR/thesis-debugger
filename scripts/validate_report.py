from pathlib import Path
import re,sys
def main():
 p=Path(sys.argv[1]) if len(sys.argv)>1 else None
 if not p or not p.is_file(): print('usage: python scripts/validate_report.py REPORT.md'); return 2
 t=p.read_text(encoding='utf-8'); errs=[]
 heads=re.findall(r'^## (\d+)\. .+$',t,re.M)
 if heads!=[(str(i)) for i in range(1,22)]: errs.append('exact 21-section heading numbering failed')
 ids=re.findall(r'^### (M\d{2}) — ',t,re.M)
 if ids!=[f'M{i:02d}' for i in range(1,23)]: errs.append('M01-M22 module order/count failed')
 for fld in ['Finding ID:','Primary Module:','Related Modules:','Location:','Problem:','Evidence:','Reasoning:','Impact:','Recommended Action:','Verification Needed:']:
  if fld not in t: errs.append('missing canonical finding field '+fld)
 if 'Audit Integrity Check' not in t: errs.append('missing integrity block')
 if errs: print('FAIL'); print('\n'.join(errs)); return 1
 print('PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
