(let ((xs '())
      (num-even 0))
  (defun add+ (x) 
         (setf xs (cons x xs))
         (if (evenp x) (setf num-even (1+ num-even))) 
         nil)

  (defun rem+ ()
         (let ((front (car xs)))
              (setf xs (cdr xs))
              (if (evenp front) (setf num-even (1- num-even)))
              front))
                 
  (defun get-num-even+ () num-even))
