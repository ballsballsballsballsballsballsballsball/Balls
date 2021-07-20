from flask import Flask as ball

deeznuts = ball(__name__)

@deeznuts.route('/')
def index():
  # do not try this your pc WILL crash if you leave this on for long enough
    return '''<script>
        var i = 1;
        while (i <= Infinity) {
            document.write("balls<br>");
            setInterval(0.5)
            i += 1;
        }
        </script>'''

if __name__ == "__main__":
    deeznuts.run(debug=True)
