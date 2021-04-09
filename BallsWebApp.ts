import * as express from "express";
const app = express()
app.use('/', (req: express.Request, res: express.Response) => res.send("balls"))

for (i = 0; i < 300; i++) {
  console.log(`balls ${i}`)                    
}

app.listen(3000, () => console.log("balls"))
