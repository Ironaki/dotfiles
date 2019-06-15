;; 1. Personal Packages
(prelude-require-packages '(smex
                            evil
                            window-numbering
                            solarized-theme
                            linum-relative
                            org-bullets
                            nlinum
                            ledger-mode))


;; 2. Essential Editing Config
;; Switch Delete and C-h
;; Make C-h delete backward, <delete> help
(define-key key-translation-map (kbd "C-h") (kbd "<deletechar>"))
(define-key key-translation-map (kbd "<deletechar>") (kbd "C-h"))
(global-set-key (kbd "<deletechar>") 'delete-backward-char)

;; C-k always kill the current buffer
(defun iro/kill-this-buffer ()
  "Kill the current buffer."
  (interactive)
  (kill-buffer (current-buffer)))

(global-set-key (kbd "C-x k") 'iro/kill-this-buffer)

;; 3. UI setting
;; Basic UI
(set-frame-font "Menlo 18" nil t)
(scroll-bar-mode -1) ;; no scroll bar
(setq linum-relative-backend 'display-line-numbers-mode)
(linum-relative-global-mode 1) ;; relative line number
(window-numbering-mode 1)
(setq prelude-whitespace nil) ;; whitespace mode too annoying


;; Do not use background color in terminal
(defun on-after-init ()
  (unless (display-graphic-p (selected-frame))
    (set-face-background 'default "unspecified-bg" (selected-frame))))
(add-hook 'window-setup-hook 'on-after-init)


;; dired hide details by default
(add-hook 'dired-mode-hook 'dired-hide-details-mode)

;; Smex
(setq-default smex-save-file (expand-file-name ".smex-items" user-emacs-directory))
;;(global-set-key (kbd "M-x") 'smex)
;;(global-set-key (kbd "C-x M-x") 'execute-extended-command)

;; Start with org mode
(setq initial-major-mode 'org-mode)
(setq initial-scratch-message "")


;; 4. Utilities
;; Backup and auto saving setting
(setq auto-save-file-name-transforms `((".*" , "~/.emacs.temp/" t)))
(setq backup-directory-alist
      `((".*" . , "~/.emacs.temp/")))
(setq delete-old-versions t
      kept-new-versions 6
      kept-old-versions 2
      version-control t)
(setq backup-by-copying-when-linked t)

;; Python
(setq python-shell-interpreter "ipython"
      python-shell-interpreter-args "-i --simple-prompt")
(setq python-indent-offset 4)

;; elisp
(add-hook 'elisp-mode (lambda () (smartparens-strict-mode)))

;; Org
(defun iro/org-hook ()
    (org-bullets-mode)
    (org-indent-mode)
    (setq org-ellipsis " ~~>")
    (setq truncate-lines nil)
    (setq org-image-actual-width (/ (display-pixel-width) 3)))

(setq org-todo-keyword-faces
      '(("EMERGENCY" . (:foreground "#DC143C" :weight bold))
        ("TODO" . "#808080")))

(setq org-todo-keywords
      '((sequence "TODO" "DONE")
        (sequence "PENDING" "EMERGENCY" "DEFER" "|")))

(add-hook 'org-mode-hook 'iro/org-hook)

;; Ledger
(defun iro/ledger-hook()
  (setq ledger-default-date-format ledger-iso-date-format))

(add-hook 'ledger-mode-hook 'iro/ledger-hook)

;; iBuffer
(setq ibuffer-saved-filter-groups
      '(("Main"
         ("Dired" (mode . dired-mode))
         ("Org" (name . "^.*org$"))
         ("Magit" (name . "^magit"))
         ("Shell" (or (mode . eshell-mode) (mode . shell-mode)))
         ("Python" (mode . python-mode))
         ("Emacs" (or (name . "^\\*scratch\\*$")
                      (name . "^\\*Messages\\*$")))
         ("Help" (or (name . "\\*Help\\*")
		     (name . "\\*Apropos\\*")
		     (name . "\\*info\\*")))
         ;; ("web" (or (mode . web-mode) (mode . js2-mode)))
         ;; ("mu4e" (name . "\*mu4e\*"))
         ;; ("programming" (or
         ;;                (mode . python-mode)
         ;;                (mode . c++-mode)))
         )))

(add-hook 'ibuffer-mode-hook
          (lambda ()
            (ibuffer-auto-mode 1)
            (ibuffer-switch-to-saved-filter-groups "Main")))

(setq ibuffer-show-empty-filter-groups nil)
(setq ibuffer-expert t)
