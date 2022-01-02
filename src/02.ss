(include "src/common.ss")

(define (solve-1 commands)
  (let ([position (fold-left apply-command '(0 . 0) commands)])
    (* (car position) (cdr position))))

(define (apply-command position command)
  (let ([code (car command)]
        [value (cdr command)]
        [x (car position)]
        [y (cdr position)])
    (cond
      [(eq? code 'forward) (cons (+ x value) y)]
      [(eq? code 'down) (cons x (+ y value))]
      [(eq? code 'up) (cons x (- y value))])))

(define (parse-line line)
  (let* ([size (string-length line)]
         [first-chunk (substring line 0 (- size 2))]
         [second-chunk (substring line (- size 1) size)])
    (cons (string->symbol first-chunk) (string->number second-chunk))))

(let ([commands (map parse-line (readlines (cadr (command-line))))])
  (printf "~s\n" (solve-1 commands)))
