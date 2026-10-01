# Git & VS Code – Öğrendiklerim

Bu doküman, **RPA Architect Learning** yolculuğunda öğrendiğim Git, GitHub, VS Code ve temel terminal kullanımını hatırlamak için hazırlanmıştır.

Amaç komutları ezberlemek değil; **hangi durumda hangi komutu kullanmam gerektiğini hatırlamaktır.**

---

# 1. Git'in Temel Mantığı

Git, projede yaptığım değişikliklerin geçmişini tutan bir **version control system**'dır.

Temel akış:

```text
Working Directory
       ↓
    git add
       ↓
Staging Area
       ↓
   git commit
       ↓
Local Repository
       ↓
    git push
       ↓
Remote Repository (GitHub)
```

### Working Directory

Üzerinde aktif olarak çalıştığım dosyalardır.

Örneğin README.md dosyasını değiştirdiğimde değişiklik ilk olarak burada bulunur.

### Staging Area

Bir sonraki commit'e hangi değişikliklerin gireceğini belirlediğim ara alandır.

```bash
git add README.md
```

veya:

```bash
git add .
```

### Local Repository

Commit yaptığımda değişiklik bilgisayarımın yerel Git geçmişine kaydedilir.

```bash
git commit -m "Update README"
```

Bu işlem henüz GitHub'a göndermez.

### Remote Repository

GitHub gibi uzaktaki repository'dir.

Local commitleri göndermek için:

```bash
git push
```

kullanılır.

---

# 2. Repository Durumunu Kontrol Etmek

En sık kullanacağım komutlardan biri:

```bash
git status
```

Repository'nin mevcut durumunu gösterir.

Örneğin:

```text
modified
untracked
staged
ahead
behind
clean
```

durumlarını buradan görebilirim.

Günlük çalışma sırasında sık sık kullanmalıyım.

---

# 3. Değişiklikleri Görmek – git diff

Dosyada ne değiştirdiğimi görmek için:

```bash
git diff
```

kullanılır.

Örneğin README'ye yeni bir satır eklediğimde:

```diff
+ New line
```

şeklinde görebilirim.

Önemli:

Dosyayı `git add` ile stage ettikten sonra normal:

```bash
git diff
```

boş görünebilir.

Staged değişiklikleri görmek için:

```bash
git diff --staged
```

kullanılır.

---

# 4. Dosyaları Stage Etmek – git add

Belirli bir dosyayı:

```bash
git add README.md
```

Bütün değişiklikleri:

```bash
git add .
```

ile stage edebilirim.

İyi çalışma alışkanlığı:

```bash
git add .
git status
git commit -m "..."
```

`git add .` sonrasında `git status` çalıştırarak yanlış bir dosyayı commit'e eklemediğimi kontrol etmeliyim.

---

# 5. Commit Oluşturmak

Stage edilen değişiklikleri Git geçmişine kaydetmek için:

```bash
git commit -m "Add learning progress"
```

kullanılır.

Commit'i projenin bir **save point / checkpoint** noktası gibi düşünebilirim.

İyi commit mesajları:

```text
Add API integration
Fix invoice validation
Update SQL exercises
Add Git ignore rules
```

Kötü örnekler:

```text
update
test
stuff
asd
```

Commit mesajı yapılan değişikliği anlatmalıdır.

---

# 6. Commit Geçmişini Görmek

Basit geçmiş:

```bash
git log --oneline
```

Örneğin:

```text
058c5ae Add remote practice section
ed47146 Merge branch 'feature/conflict-practice'
26031dc Complete Git workflow on main
```

Branch'lerle beraber grafik olarak görmek için:

```bash
git log --oneline --graph --decorate --all
```

Bu özellikle branch ve merge işlemlerini anlamak için faydalıdır.

---

# 7. HEAD Nedir?

HEAD, şu anda üzerinde bulunduğum commit/branch konumunu gösterir.

Örneğin:

```text
HEAD -> main
```

şu anda `main` branch üzerinde olduğumu gösterir.

---

# 8. origin/main Nedir?

`origin/main`, GitHub'daki `main` branch hakkında local Git'in bildiği son durumu temsil eden **remote-tracking branch**'tir.

Önemli:

`origin/main` GitHub'a canlı bağlı bir gösterge değildir.

Remote'daki son durumu öğrenmek için:

```bash
git fetch
```

kullanmam gerekir.

---

# 9. Push

Local commitleri GitHub'a göndermek için:

```bash
git push
```

kullanılır.

Örneğin:

```text
Local:

A → B → C
        ↑
       main

GitHub:

A → B
    ↑
origin/main
```

`git push` sonrasında:

```text
A → B → C
        ↑
 main / origin/main
```

olur.

---

# 10. Fetch

GitHub'daki yeni commitleri ve branch bilgilerini öğrenmek için:

```bash
git fetch
```

kullanılır.

Fetch:

- Remote bilgilerini günceller.
- `origin/main` gibi remote-tracking branch'leri günceller.
- Çalıştığım dosyaları doğrudan değiştirmez.
- Local `main` branch'imi otomatik olarak ilerletmez.

Biz bunu GitHub üzerinden README'ye doğrudan değişiklik yaparak test ettik.

Fetch öncesinde Git:

```text
main → ed47146
origin/main → ed47146
```

sanıyordu.

GitHub'da yeni commit olmasına rağmen local Git henüz bilmiyordu.

`git fetch` sonrasında:

```text
main → ed47146
             \
              058c5ae ← origin/main
```

oldu.

---

# 11. Remote'da Ne Değiştiğini İncelemek

Remote'da olup local `main` branch'imde olmayan commitleri görmek için:

```bash
git log main..origin/main --oneline
```

kullanabilirim.

Kod/dosya farklarını görmek için:

```bash
git diff main..origin/main
```

kullanabilirim.

Güvenli çalışma şekli:

```text
git fetch
    ↓
git log main..origin/main --oneline
    ↓
git diff main..origin/main
    ↓
git pull
```

Önce ne geleceğini görürüm, sonra local'e alırım.

---

# 12. Pull

Remote değişikliklerini local branch'ime almak için:

```bash
git pull
```

kullanılır.

Basitleştirilmiş şekilde:

```text
git pull
≈
git fetch
+
remote değişikliklerini local branch'e entegre et
```

Biz GitHub'da oluşturduğumuz:

```text
Add remote practice section
```

commit'ini `git pull` ile local bilgisayarımıza aldık.

---

# 13. Clone

GitHub'da zaten bulunan bir repository'yi bilgisayarıma ilk kez almak için:

```bash
git clone <repository-url>
```

kullanılır.

Biz:

```bash
git clone https://github.com/ozaysevinc/rpa-architect-learning.git rpa-architect-learning-clone
```

kullanarak test yaptık.

Clone:

```text
dosyaları indirir
+
Git geçmişini indirir
+
.git oluşturur
+
origin remote'unu ayarlar
+
default branch'i hazırlar
```

Bu nedenle mevcut bir projeyi bilgisayarıma alırken tekrar:

```text
git init
git remote add ...
```

yapmam gerekmez.

---

# 14. Remote Kontrolü

Repository'nin bağlı olduğu remote adreslerini görmek için:

```bash
git remote -v
```

kullanılır.

`fetch` ve `push` adreslerini gösterir.

---

# 15. Değişiklikten Vazgeçmek – git restore

Dosyada değişiklik yaptım ancak henüz stage etmedim.

Değişiklikten tamamen vazgeçmek için:

```bash
git restore README.md
```

kullanabilirim.

Bu işlem commit edilmemiş değişikliği silebildiği için dikkatli kullanılmalıdır.

---

# 16. Staging'den Çıkarmak

Dosyayı:

```bash
git add README.md
```

ile stage ettim ama commit'e dahil etmekten vazgeçtim.

Değişikliği kaybetmeden staging'den çıkarmak için:

```bash
git restore --staged README.md
```

kullanılır.

Akış:

```text
STAGED
   ↓
git restore --staged
   ↓
MODIFIED
```

Dosyadaki değişiklik korunur.

---

# 17. Revert

Commit edilmiş bir değişikliğin tersini yapan yeni bir commit oluşturmak için:

```bash
git revert <commit-hash>
```

kullanılır.

Biz:

```bash
git revert ffff76b
```

deneyini yaptık.

Sonuç:

```text
A → B → C → D
        ↑    ↑
      hata  C'yi geri alan commit
```

`C` geçmişten silinmedi.

Özellikle başkalarıyla paylaşılmış / push edilmiş commitlerde geçmişi koruyarak düzeltme yapmak için kullanışlıdır.

---

# 18. Reset

Branch'in işaret ettiği commit'i geçmişte başka bir noktaya taşımak için kullanılabilir.

### Soft

```bash
git reset --soft <commit>
```

Commit geri alınır fakat değişiklikler staged kalır.

### Mixed

```bash
git reset <commit>
```

Commit geri alınır, değişiklikler Working Directory'de kalır.

### Hard

```bash
git reset --hard <commit>
```

Commit geri alınır ve ilgili çalışma değişiklikleri de atılabilir.

`--hard` veri kaybına yol açabileceğinden ne yaptığımı bilmeden kullanmamalıyım.

Biz eğitim sırasında kontrollü şekilde:

```bash
git reset --hard ba2b869
```

kullandık.

---

# 19. Geri Alma Karar Şeması

Pratik kural:

```text
Hata yaptım
    │
    ▼
Commit ettim mi?
 │             │
Hayır         Evet
 │             │
 ▼             ▼
Staged?     Push ettim mi?
 │             │
 ├─ Hayır      ├─ Hayır → reset düşünülebilir
 │   restore   │
 │             └─ Evet → revert düşün
 └─ Evet
     restore --staged
```

Kısa hali:

```text
Değiştirdim       → restore
Stage ettim       → restore --staged
Local commit      → reset düşünülebilir
Push edilmiş      → revert düşün
```

---

# 20. Branch

Yeni bir geliştirmeyi `main`den bağımsız yapmak için branch kullanılır.

Yeni branch oluşturup geçmek:

```bash
git switch -c feature/api-integration
```

Mevcut branch'leri görmek:

```bash
git branch
```

Örneğin:

```text
* feature/api-integration
  main
```

`*` aktif branch'i gösterir.

Branch değiştirmek:

```bash
git switch main
```

Branch, projenin komple ikinci bir kopyası değildir.

Temelde commit geçmişindeki bir noktayı gösteren hafif bir referanstır.

---

# 21. Branch İsimlendirme

Örnekler:

```text
feature/api-integration
feature/sql-reporting
fix/login-error
docs/update-readme
```

Bunlar Git zorunluluğu değildir; projeyi düzenli tutmak için kullanılan isimlendirme yaklaşımlarıdır.

---

# 22. Merge

Bir branch'teki çalışmayı başka bir branch'e almak için:

```bash
git merge <branch>
```

kullanılır.

Önemli kural:

> Değişikliği hangi branch'in içine almak istiyorsam önce o branch'e geçerim.

Örneğin feature'ı `main`e almak:

```bash
git switch main
git merge feature/api-integration
```

---

# 23. Fast-Forward Merge

Feature branch ayrıldıktan sonra `main` ilerlemediyse Git sadece `main` pointer'ını ileri taşıyabilir.

Önce:

```text
A → B
     \
      C ← feature
```

Merge sonrası:

```text
A → B → C
        ↑
       main
```

Yeni merge commit'i gerekmeyebilir.

Biz ilk branch pratiğimizde bunu gördük.

---

# 24. Merge Conflict

İki branch aynı satırı farklı şekilde değiştirirse Git hangi değişikliğin doğru olduğuna kendi karar veremez.

Örneğin:

Main:

```text
Git daily workflow - completed on main branch
```

Feature:

```text
Git daily workflow - completed on feature branch
```

Merge sırasında:

```text
CONFLICT (content)
```

oluştu.

Bu Git'in bozulduğu anlamına gelmez.

Git:

> Bu kısmı otomatik çözemiyorum, insan kararı gerekiyor.

demektedir.

---

# 25. Current ve Incoming Change

Merge sırasında:

```bash
git switch main
git merge feature/test
```

yaptıysam:

```text
CURRENT  = main
INCOMING = feature/test
```

VS Code seçenekleri:

```text
Accept Current Change
Accept Incoming Change
Accept Both Changes
Compare Changes
```

### Current

Şu anda üzerinde bulunduğum branch'in değişikliğini tutar.

### Incoming

Merge etmeye çalıştığım branch'ten gelen değişikliği tutar.

### Both

İki değişikliği de tutar.

Gerekirse hiçbirini doğrudan seçmeden dosyayı manuel olarak da düzenleyebilirim.

---

# 26. Conflict Çözüm Akışı

Bizim uyguladığımız süreç:

```text
git merge feature/conflict-practice
        ↓
CONFLICT
        ↓
VS Code'da doğru içeriği seç/düzenle
        ↓
Kaydet
        ↓
git add README.md
        ↓
Git'e "conflict çözüldü" bilgisini ver
        ↓
git commit
        ↓
Merge tamamlandı
```

Merge'i tamamen iptal etmek gerekirse Git'in gösterdiği:

```bash
git merge --abort
```

komutu kullanılabilir.

---

# 27. Merge Commit

İki branch birbirinden bağımsız ilerlemişse Git yeni bir merge commit'i oluşturabilir.

Bizim gerçek örneğimiz:

```text
            274a922 feature
           /       \
3d4bb03 --           ed47146 merge
           \       /
            26031dc main
```

`ed47146` iki geliştirme hattını birleştiren merge commit'imizdi.

Merge commit'in iki parent commit'i olabilir.

---

# 28. Branch Silmek

Merge edilmiş ve artık ihtiyacım olmayan local branch'i:

```bash
git branch -d feature/test
```

ile silebilirim.

`-d` güvenli silmedir.

Force delete:

```bash
git branch -D feature/test
```

daha agresiftir ve dikkatli kullanılmalıdır.

Branch'i silmek, merge edilmiş commitleri veya dosyaları silmez.

Sadece branch referansını kaldırır.

---

# 29. .git Klasörü

Git repository'nin içerisinde gizli:

```text
.git/
```

klasörü bulunur.

Burada repository'nin Git metadata'sı ve geçmişine ilişkin veriler tutulur.

Clone deneyinde:

```powershell
Get-ChildItem -Force
```

ile `.git` klasörünü gördük.

`.git` içeriğini normal çalışma sırasında elle değiştirmemeliyim.

---

# 30. Repository Root'u Bulmak

Terminalde hangi repository içinde olduğumu karıştırırsam:

```bash
git rev-parse --show-toplevel
```

kullanabilirim.

Bu bana repository'nin root klasörünü gösterir.

---

# 31. .gitignore

Git'in belirli dosya ve klasörleri takip etmemesi için:

```text
.gitignore
```

kullanılır.

Biz repository root'una `.gitignore` oluşturduk.

İçeriğimiz:

```gitignore
# Environment variables / secrets
.env
.env.*

# Python virtual environments
.venv/
venv/

# Python cache
__pycache__/
*.pyc

# VS Code local settings
.vscode/

# OS files
.DS_Store
Thumbs.db
```

---

# 32. .env Neden Önemli?

İleride:

```text
API_KEY
password
token
secret
connection string
```

gibi bilgileri `.env` içerisinde tutabiliriz.

Örneğin:

```text
OPENAI_API_KEY=...
```

Bu dosyanın GitHub'a gitmesini istemeyiz.

Bu yüzden:

```gitignore
.env
.env.*
```

kuralını ekledik.

Temel güvenlik kuralı:

> API key, parola ve token gibi secret bilgileri Git repository'ye commit etme.

---

# 33. git check-ignore

Bir dosyanın gerçekten ignore edilip edilmediğini kontrol etmek için:

```bash
git check-ignore -v .env
```

kullandık.

Bizde:

```text
.gitignore:2:.env    .env
```

çıktısı geldi.

Anlamı:

```text
.gitignore
    ↓
2. satır
    ↓
.env kuralı
    ↓
.env dosyasını ignore ediyor
```

---

# 34. Yaptığımız Gerçek Git Akışı

Eğitim sırasında sıfırdan:

```text
Local proje
    ↓
git init
    ↓
README oluşturma
    ↓
git add
    ↓
ilk commit
    ↓
GitHub remote bağlantısı
    ↓
git push
    ↓
değişiklik yapma
    ↓
diff / staging / commit
    ↓
restore
    ↓
restore --staged
    ↓
revert
    ↓
reset
    ↓
branch
    ↓
feature geliştirme
    ↓
fast-forward merge
    ↓
merge conflict
    ↓
conflict çözme
    ↓
merge commit
    ↓
push
    ↓
fetch
    ↓
remote değişikliklerini inceleme
    ↓
pull
    ↓
clone
    ↓
.gitignore
```

Bu nedenle bu komutları yalnızca okumadım; gerçek repository üzerinde uyguladım.

---

# 35. Günlük Kullanacağım Workflow

Normal geliştirme sırasında:

```bash
git status
```

Kodumu değiştiririm.

Sonra:

```bash
git diff
```

Ne değiştirdiğimi kontrol ederim.

Ardından:

```bash
git add .
git status
```

Commit'e girecek dosyaları kontrol ederim.

Sonra:

```bash
git commit -m "Meaningful commit message"
git push
```

---

# 36. Feature Geliştirme Workflow

Yeni özellik geliştirirken:

```bash
git switch main
git pull
git switch -c feature/my-feature
```

Kodumu geliştiririm.

Sonra:

```bash
git status
git diff
git add .
git status
git commit -m "Add my feature"
```

Feature tamamlandığında uygun ekip/repository workflow'una göre branch merge veya Pull Request süreci uygulanır.

Eğitimde local merge'i şöyle yaptık:

```bash
git switch main
git merge feature/my-feature
git push
git branch -d feature/my-feature
```

---

# 37. Remote Kontrol Workflow

GitHub'da başkalarının değişiklik yapmış olabileceği bir projede:

```bash
git fetch
```

Sonra:

```bash
git log main..origin/main --oneline
```

ve gerekirse:

```bash
git diff main..origin/main
```

ile değişiklikleri incelerim.

Ardından uygun olduğunda:

```bash
git pull
```

ile local branch'imi güncellerim.

---

# 38. En Çok Kullanacağım Komutlar

```bash
git status
git diff
git add .
git commit -m "..."
git push
git pull
git fetch

git switch main
git switch -c feature/name

git branch
git merge branch-name

git log --oneline
git log --oneline --graph --decorate --all
```

Bunlar günlük geliştirme hayatımda Git kullanımımın büyük bölümünü oluşturacaktır.

---

# 39. Sorun Çıktığında Önce Ne Yapmalıyım?

Panikleyip `reset --hard`, `-D`, force push gibi güçlü komutlara geçmeden önce:

```bash
git status
```

çalıştır.

Sonra gerekirse:

```bash
git log --oneline --graph --decorate --all
```

ile nerede olduğumu kontrol et.

Temel yaklaşım:

```text
Önce durumu anla
      ↓
Sonra değişikliği gör
      ↓
Sonra doğru Git komutunu seç
```

Git çoğu zaman `git status` çıktısında bir sonraki yapılabilecek işlemi de söyler.

---

# 40. Şu Anki Seviyem

Tamamlanan temel konular:

- [x] VS Code'da repository ile çalışma
- [x] PowerShell terminal kullanımı
- [x] Git repository oluşturma
- [x] GitHub remote bağlantısı
- [x] Add / Stage
- [x] Commit
- [x] Push
- [x] Diff
- [x] Git history
- [x] Restore
- [x] Restore staged
- [x] Revert
- [x] Reset mantığı
- [x] Branch oluşturma
- [x] Branch değiştirme
- [x] Fast-forward merge
- [x] Merge commit
- [x] Merge conflict çözme
- [x] Branch silme
- [x] Fetch
- [x] Pull
- [x] Clone
- [x] `.git` mantığı
- [x] `.gitignore`
- [x] Secret dosyalarını Git dışında tutma

Daha sonra gerçek projeler sırasında öğreneceğim ileri konular:

- [ ] GitHub Pull Request
- [ ] Code Review
- [ ] `git stash`
- [ ] `git rebase`
- [ ] `git cherry-pick`
- [ ] Tag / Release
- [ ] Branch protection
- [ ] CI/CD ile Git entegrasyonu

---

# Hızlı Hatırlatma

```text
Repository durumuna bak        → git status

Ne değiştirdim?                → git diff

Commit'e hazırla               → git add .

Commit oluştur                 → git commit -m "..."

GitHub'a gönder                → git push

GitHub'daki yenilikleri öğren  → git fetch

Remote değişikliklerini al     → git pull

Projeyi ilk kez indir          → git clone

Yeni branch                    → git switch -c <branch>

Branch değiştir                → git switch <branch>

Branch birleştir               → git merge <branch>

Branch sil                     → git branch -d <branch>

Değişiklikten vazgeç           → git restore <file>

Staging'den çıkar              → git restore --staged <file>

Commit'i tersine çevir         → git revert <hash>

Geçmişi gör                    → git log --oneline

Branch grafiğini gör           → git log --oneline --graph --decorate --all

Ignore kontrol et              → git check-ignore -v <file>

Repository root'unu bul        → git rev-parse --show-toplevel
```

## Ana Kural

**Git'te emin olmadığım bir durumda önce `git status` çalıştırırım.**

Özellikle `reset --hard`, force delete veya ileride göreceğim force push gibi geçmişi/değişiklikleri etkileyebilecek komutları ne yaptığımı anlamadan kullanmam.