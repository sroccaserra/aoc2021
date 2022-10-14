(require "uiop")

(defun get-lines ()
  (let ((filename (first (uiop:command-line-arguments))))
    (loop for line in (uiop:read-file-lines filename)
          collect (parse-integer line))))

(defun solve (numbers)
  (let ((result 0)
        (previous 9999))
    (loop for n in numbers do
          (when (> n previous)
            (setq result (+ 1 result)))
          (setq previous n))
    result))

(let ((numbers (get-lines)))
  (write-line (write-to-string (solve numbers))))
