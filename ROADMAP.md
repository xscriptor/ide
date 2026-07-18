# IDE Xscriptor — Roadmap

## Phase 1: Core Theme Library <!-- phase:core-themes -->

- [x] Define base color palette reference (colors.md) (#3)
- [x] Create theme: X (#4)
- [x] Create theme: Madrid (#5)
- [x] Create theme: Lahabana (#6)
- [x] Create theme: Miami (#7)
- [x] Create theme: Paris (#8)
- [x] Create theme: Tokio (#9)
- [x] Create theme: Oslo (#10)
- [x] Create theme: Helsinki (#11)
- [x] Create theme: Berlin (#12)
- [x] Create theme: London (#13)
- [x] Create theme: Praha (#14)
- [x] Create theme: Bogota (#15)

## Phase 2: IDE Ports (Code Editors) <!-- phase:code-editor-ports -->

- [x] Port themes to VS Code (.json ColorTheme)
- [ ] Port themes to Sublime Text (.sublime-color-scheme)
- [ ] Port themes to TextMate (.tmTheme)
- [ ] Port themes to Vim (.vim colorscheme)
- [ ] Port themes to Neovim (.lua colorscheme)
- [ ] Port themes to Emacs (color theme)
- [ ] Port themes to Helix (.toml themes)
- [ ] Port themes to Zed (.json themes)
- [ ] Port themes to Lite XL (.lua themes)
- [ ] Port themes to Micro (.json themes)
- [ ] Port themes to Geany (.scheme files)
- [ ] Port themes to Kate (.theme files)
- [ ] Port themes to Gedit (.xml theme files)
- [ ] Port themes to Notepad++ (.xml theme files)
- [ ] Port themes to CudaText (.json themes)
- [ ] Port themes to BBEdit (.bbcolorproject)
- [ ] Port themes to Kakoune (.kak theme)

## Phase 3: IDE Ports (Full IDEs & Platforms) <!-- phase:full-ide-ports -->

- [x] Port themes to IntelliJ IDEA / JetBrains Suite (.icls / .jar)
- [ ] Port themes to Eclipse (.epf color themes)
- [ ] Port themes to NetBeans (.zip theme)
- [ ] Port themes to Visual Studio (.vssettings)
- [ ] Port themes to Android Studio (.icls)
- [ ] Port themes to Qt Creator (.creatortheme)
- [ ] Port themes to Code::Blocks (.conf)
- [ ] Port themes to Spyder (.py / .qss themes)
- [ ] Port themes to RStudio (.tmTheme)
- [ ] Port themes to Arduino IDE 2.x (JSON themes)
- [ ] Port themes to Lazarus IDE (.xml themes)
- [ ] Port themes to CodeLite (.json themes)

## Phase 4: IDE Ports (Modern & Cloud IDEs) <!-- phase:modern-ide-ports -->

- [ ] Port themes to Nova (Panic, .novaextension)
- [x] Port themes to Fleet (JetBrains, JSON themes)
- [x] Port themes to Cursor (VS Code fork, ColorTheme)
- [x] Port themes to Windsurf (VS Code fork, ColorTheme)
- [ ] Port themes to Replit (themes)
- [ ] Port themes to CodeSandbox (themes)
- [ ] Port themes to Jupyter Lab (theme JSON)

## Phase 5: Install & Uninstall Scripts <!-- phase:install-scripts -->

- [x] Install script for VS Code (install.sh)
- [x] Install script for Sublime Text (install.sh)
- [ ] Install script for TextMate (install.sh)
- [ ] Install script for Vim (install.sh)
- [ ] Install script for Neovim (install.sh)
- [ ] Install script for Emacs (install.sh)
- [ ] Install script for Helix (install.sh)
- [ ] Install script for Zed (install.sh)
- [ ] Install script for Lite XL (install.sh)
- [ ] Install script for Micro (install.sh)
- [ ] Install script for Geany (install.sh)
- [ ] Install script for Kate (install.sh)
- [ ] Install script for Gedit (install.sh)
- [ ] Install script for Notepad++ (install.ps1)
- [x] Install script for IntelliJ IDEA / JetBrains (install.sh)
- [ ] Install script for Eclipse (install.sh)
- [ ] Install script for NetBeans (install.sh)
- [ ] Install script for Visual Studio (install.ps1)
- [ ] Install script for Android Studio (install.sh)
- [ ] Install script for Qt Creator (install.sh)
- [ ] Install script for Nova (install.sh)
- [ ] Install script for Fleet (install.sh)
- [ ] Install script for Jupyter Lab (install.sh)

- [x] Uninstall script for VS Code (uninstall.sh)
- [/] Uninstall script for Sublime Text (uninstall.sh)
- [ ] Uninstall script for TextMate (uninstall.sh)
- [ ] Uninstall script for Vim (uninstall.sh)
- [ ] Uninstall script for Neovim (uninstall.sh)
- [ ] Uninstall script for Emacs (uninstall.sh)
- [ ] Uninstall script for Helix (uninstall.sh)
- [ ] Uninstall script for Zed (uninstall.sh)
- [ ] Uninstall script for Lite XL (uninstall.sh)
- [ ] Uninstall script for Micro (uninstall.sh)
- [ ] Uninstall script for Notepad++ (uninstall.ps1)
- [x] Uninstall script for IntelliJ IDEA / JetBrains (uninstall.sh)
- [ ] Uninstall script for Eclipse (uninstall.sh)
- [ ] Uninstall script for NetBeans (uninstall.sh)
- [ ] Uninstall script for Visual Studio (uninstall.ps1)
- [ ] Uninstall script for Android Studio (uninstall.sh)
- [ ] Uninstall script for Qt Creator (uninstall.sh)
- [ ] Uninstall script for Nova (uninstall.sh)
- [ ] Uninstall script for Jupyter Lab (uninstall.sh)

- [ ] Per-IDE reset.sh to restore original configs

## Phase 6: Documentation & Previews <!-- phase:documentation -->

- [x] Main project README.md with monorepo structure
- [x] Xcode README.md with install instructions
- [x] README for VS Code
- [x] README for Sublime Text
- [ ] README for TextMate
- [ ] README for Vim / Neovim
- [ ] README for Emacs
- [ ] README for Helix
- [ ] README for Zed
- [ ] README for Lite XL
- [ ] README for Micro
- [ ] README for Geany
- [ ] README for Kate
- [ ] README for Gedit
- [ ] README for Notepad++
- [ ] README for CudaText
- [ ] README for BBEdit
- [x] README for IntelliJ IDEA / JetBrains Suite
- [ ] README for Eclipse
- [ ] README for NetBeans
- [ ] README for Visual Studio
- [ ] README for Android Studio
- [ ] README for Qt Creator
- [ ] README for Code::Blocks
- [ ] README for Spyder
- [ ] README for RStudio
- [ ] README for Nova
- [ ] README for Fleet
- [ ] README for Jupyter Lab

- [x] Previews for VS Code
- [/] Previews for Sublime Text
- [ ] Previews for Vim / Neovim
- [x] Previews for IntelliJ IDEA / JetBrains
- [ ] Previews for Visual Studio
- [ ] Previews for Eclipse
- [ ] Quick import guides per platform (Linux/macOS/Windows)
- [ ] Troubleshooting section per IDE (paths, caches, quirks)
- [ ] Support policy and compatibility matrix by IDE / version
- [ ] Contribution template for new ports and PR guidelines

## Phase 7: Tooling & Automation <!-- phase:tooling -->

- [ ] CLI tool ide-theme to apply schemes from shell (#134)
- [ ] Linter for file structure and required keys per IDE (#135)
- [ ] Contrast and accessibility report (WCAG compliance) (#136)
- [x] Set up .github/scripts/sync_roadmap.py for Roadmap Sync (#137)
- [x] Set up .github/workflows/roadmap-sync.yml GitHub Action (#138)

## Phase 8: Integrations & Ecosystem <!-- phase:integrations -->

- [ ] Theme companion for terminal emulators (match IDE + terminal colors) (#139)
- [ ] Shell syntax-highlighting theme matching (zsh-syntax-highlighting, fish) (#140)
- [ ] Cross-IDE theme sync tool (apply same palette everywhere) (#141)

## Phase 9: Packaging & Releases <!-- phase:packaging -->

- [x] Packaging: VS Code extension (.vsix)
- [/] Packaging: Sublime Text Package Control
- [x] Packaging: JetBrains plugin repository
- [ ] Packaging: Homebrew Tap for macOS
- [ ] Releases with semantic versioning and changelog
- [ ] Quarterly roadmap with measurable goals and milestones
