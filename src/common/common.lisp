(require "asdf")

(defun get-parsed-lines (parse-fn)
  (let ((filename (first (uiop:command-line-arguments))))
    (loop for line in (uiop:read-file-lines filename)
          collect (funcall parse-fn line))))

(provide "common")
