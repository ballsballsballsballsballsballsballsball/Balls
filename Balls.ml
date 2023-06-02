let rec balls b a ll s =
  if b <> "b" then (balls a ll s b) else (b ^ a ^ ll ^ s);;

Printf.printf "%s\n" (balls "a" "ll" "s" "b");;
