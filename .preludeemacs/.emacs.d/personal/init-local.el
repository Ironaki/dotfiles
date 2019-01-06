;; Switch Delete and C-h
(define-key key-translation-map (kbd "C-h") (kbd "<deletechar>"))
(define-key key-translation-map (kbd "<deletechar>") (kbd "C-h"))
(global-set-key (kbd "<deletechar>") 'delete-backward-char)

;; Set font
(set-frame-font "Menlo 18" nil t)

;; Personal Packages
(prelude-require-packages '(smex
                            evil
                            window-numbering))

(window-numbering-mode 1)

(setq-default smex-save-file (expand-file-name ".smex-items" user-emacs-directory))
(global-set-key (kbd "M-x") 'smex)
(global-set-key (kbd "C-x M-x") 'execute-extended-command)

;; C-k always kill the current buffer
(defun iro/kill-this-buffer ()
  "Kill the current buffer."
  (interactive)
  (kill-buffer (current-buffer)))

(global-set-key (kbd "C-x k") 'iro/kill-this-buffer)


