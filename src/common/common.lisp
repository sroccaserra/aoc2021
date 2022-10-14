(require "uiop")

(defun get-lines ()
  (let ((filename (first (uiop:command-line-arguments))))
    (loop for line in (uiop:read-file-lines filename)
          collect (parse-integer line))))

(provide "common")
