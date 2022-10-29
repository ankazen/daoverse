require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
        solidity: {
            compilers: [{
                    version: "0.6.0",
                },
                {
                    version: "0.8.0",
                },
                {
                    version: "0.8.12",
                },
                {
                    version: "0.8.9",
                },
                {
                    version: "0.8.1",
                },
                {
                    version: "0.8.4",
                },
                {
                    version: "0.8.13",
                },
            ],
        },
         gas: 2100000,
   gasPrice: 8000000000,
}