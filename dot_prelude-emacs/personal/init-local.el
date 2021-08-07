;; 1. Personal Packages
(prelude-require-packages '(smex
                            evil
                            window-numbering
                            solarized-theme
                            linum-relative
                            org-superstar
                            nlinum                            
                            ledger-mode
                            ob-ipython
                            org-present
                            whitespace-cleanup-mode
                            htmlize
                            multiple-cursors))

(exec-path-from-shell-copy-envs '("LC_ALL"))

;; 2. Essential Editing Config
;; Change Ctrl-h to backspace (Done by karabiner; Commented out)/ Change backspace key to help
;; <deletechar> is delete forward
;; <backsapce> is translated automatically to DEL, which is delete backward
;; (define-key key-translation-map (kbd "C-h") (kbd "<deletechar>"))
;; (define-key key-translation-map (kbd "<deletechar>") (kbd "C-h"))
;; press fn+delete for help
(define-key key-translation-map (kbd "<deletechar>") (kbd "C-h"))

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
(global-nlinum-mode 0)
(global-visual-line-mode 1)
(global-whitespace-cleanup-mode 1)
(setq-default line-spacing 3)



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
    (org-superstar-mode)
    (org-indent-mode)
    (setq org-ellipsis " ~~>")
    (visual-line-mode)
    ;;(setq truncate-lines nil)
    (setq org-image-actual-width (/ (display-pixel-width) 3)))

(setq org-todo-keyword-faces
      '(("EMERGENCY" . (:foreground "#DC143C" :weight bold))
        ("TODO" . "#808080")))

(setq org-todo-keywords
      '((sequence "TODO" "DONE")
        (sequence "PENDING" "EMERGENCY" "DEFER" "|")))

(add-hook 'org-mode-hook 'iro/org-hook)


;; Org literate programming
(org-babel-do-load-languages
 'org-babel-load-languages
 '(
   (python . t)
   ;; (ipython . t)
   ;; (sh . t)
   (shell . t)
   ;; (scala . t)
   ;; Include other languages here...
   ))

;; Don't prompt before running code in org
(setq org-confirm-babel-evaluate nil)

(eval-after-load "org-present"
  '(progn
     (add-hook 'org-present-mode-hook
               (lambda ()
                 (org-present-big)
                 (org-display-inline-images)
                 (org-present-hide-cursor)
                 (org-present-read-only)))
     (add-hook 'org-present-mode-quit-hook
               (lambda ()
                 (org-present-small)
                 (org-remove-inline-images)
                 (org-present-show-cursor)
                 (org-present-read-write)))))
;; Fix an incompatibility between the ob-async and ob-ipython packages
;; (setq ob-async-no-async-languages-alist '("ipython"))

;; Ledger
(defun iro/ledger-hook()
  (setq ledger-default-date-format ledger-iso-date-format))

(add-hook 'ledger-mode-hook 'iro/ledger-hook)

;; iBuffer
(setq ibuffer-saved-filter-groups
      '(("Main"
         ("Dired" (mode . dired-mode))
         ("Python" (mode . python-mode))
         ("Org" (name . "^.*org$"))
         ("Shell" (or (mode . eshell-mode) (mode . shell-mode)))
         ("Emacs" (or (name . "^\\*scratch\\*$")
                      (name . "^\\*Messages\\*$")))
         ("Magit" (name . "^magit"))         
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
            (visual-line-mode -1)
            (setq truncate-lines t)
            (ibuffer-switch-to-saved-filter-groups "Main")))

(setq ibuffer-show-empty-filter-groups nil)
(setq ibuffer-expert t)

(setq ibuffer-formats
      '((mark modified read-only " "
              (name 40 40 :left :elide) ; change: 30s were originally 18s
              " " ;; between columns
              ;; (size 9 -1 :right)
              ;; " "
              (mode 16 16 :left :elide)
              " " filename-and-process)
        (mark " "
              (name 60 60 :left :elide)
              " " filename)))

(setq markdown-command "pandoc -f gfm \
                               -t html5 \
                               --mathjax \
                               --quiet \
                               --standalone \
                               --highlight-style tango \
                               --css ~/.pandoc/github-pandoc.css")


;; Multiple cursors
(global-set-key (kbd "C-S-c C-S-c") 'mc/edit-lines)
(global-set-key (kbd "C->") 'mc/mark-next-like-this)
(global-set-key (kbd "C-<") 'mc/mark-previous-like-this)
(global-set-key (kbd "C-c C-<") 'mc/mark-all-like-this)
