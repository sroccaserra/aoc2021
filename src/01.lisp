(require "common" "src/common/common.lisp")

(defconstant HUGE 9999)

(defun solve-1 (numbers)
  (let ((result 0)
        (previous HUGE))
    (dolist (n numbers)
      (when (> n previous)
        (setq result (+ 1 result)))
      (setq previous n))
    result))

(defun solve-2 (numbers)
  (let ((result 0)
        (p1 HUGE)
        (p2 HUGE)
        (p3 HUGE))
    (dolist (n numbers)
      (when (> (+ n p1 p2) (+ p1 p2 p3))
        (setq result (+ 1 result)))
      (setq p3 p2
            p2 p1
            p1 n))
    result))

(let ((numbers (get-parsed-lines #'parse-integer)))
  (format t "~d~%" (solve-1 numbers))
  (format t "~d~%" (solve-2 numbers)))
