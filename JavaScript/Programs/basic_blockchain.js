const SHA256 = require('crypto-js/sha256');

class Block {
    constructor(data) {
            this.hash = "",
            this.height = 0,
            this.body = data,
            this.time = 0,
            this.previousBlockHash = "";
    }
}

class BlockChain{
    constructor(){
        this.chain = [];
        this.addBlock(new Block("First block in the chain - Genesis block"));
    }

    addBlock(newBlock){
        if(this.chain.length>0){
            newBlock.previousBlockHash = this.chain[this.chain.length-1].hash;
        }
        newBlock.height = this.chain.length;
        newBlock.time = new Date().getTime().toString().slice(0, -3);
        newBlock.hash = SHA256(JSON.stringify(newBlock)).toString();
        this.chain.push(newBlock);
    }
}