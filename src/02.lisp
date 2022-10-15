(require "uiop")

(require "common" "src/common/common.lisp")

(defun solve (commands)
  (let ((hpos 0)
        (depth-1 0)
        (depth-2 0)
        (aim 0))
    (loop for (direction value) (symbol integer) in commands do
          (cond ((eq ':|forward| direction)
                 (incf hpos value)
                 (incf depth-2 (* aim value)))
                ((eq ':|up| direction)
                 (decf depth-1 value)
                 (decf aim value))
                ((eq ':|down| direction)
                 (incf depth-1 value)
                 (incf aim value))))
    (list (* hpos depth-1) (* hpos depth-2))))

(defun parse-command (line)
  (destructuring-bind (direction value-str) (uiop:split-string line)
    (list (intern direction "KEYWORD") (parse-integer value-str))))

(let ((commands (get-parsed-lines #'parse-command)))
  (destructuring-bind (result-1 result-2) (solve commands)
    (write-line (write-to-string result-1))
    (write-line (write-to-string result-2))))
