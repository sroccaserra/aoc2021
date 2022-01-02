(include "src/common.ss")

(define (solve-1 commands)
  (let ([position (fold-left apply-command-1 '(0 . 0) commands)])
    (* (car position) (cdr position))))

(define (apply-command-1 position command)
  (let ([code (car command)]
        [value (cdr command)]
        [x (car position)]
        [y (cdr position)])
    (cond
      [(eq? code 'forward) (cons (+ x value) y)]
      [(eq? code 'down) (cons x (+ y value))]
      [(eq? code 'up) (cons x (- y value))])))

(define (solve-2 commands)
  (let ([position (fold-left apply-command-2 (make-submarine 0 0 0) commands)])
    (* (submarine-x position) (submarine-y position))))

(define (apply-command-2 submarine command)
  (let ([code (car command)]
        [value (cdr command)]
        [x (submarine-x submarine)]
        [y (submarine-y submarine)]
        [aim (submarine-aim submarine)])
    (cond
      [(eq? code 'forward) (make-submarine (+ x value) (+ y (* value aim)) aim)]
      [(eq? code 'down) (make-submarine x y (+ aim value))]
      [(eq? code 'up) (make-submarine x y (- aim value))])))

(define-record-type submarine (fields x y aim))

(define (parse-line line)
  (let* ([size (string-length line)]
         [first-chunk (substring line 0 (- size 2))]
         [second-chunk (substring line (- size 1) size)])
    (cons (string->symbol first-chunk) (string->number second-chunk))))

(let ([commands (map parse-line (readlines (cadr (command-line))))])
  (printf "~s\n" (solve-1 commands))
  (printf "~s\n" (solve-2 commands)))
