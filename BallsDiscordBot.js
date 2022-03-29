const BallsJS = require('discord.js');
const Balls   = new BallsJS.Client({ 
  intents: ["GUILDS", "GUILD_MESSAGES", "DIRECT_MESSAGES"],
  partials: ["CHANNELS"],
});
let token     = 'balls';
let prefix    = '()';

 
// Messag eenent
Balls.on('messageCreate', message => {
  if (message.content === prefix+"balls") {
      message.channel.send("BALLS")
  }
})


// READY
Balls.on('ready', () => {
  console.log("balls")
})


Balls.login(token)
