// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {
  const governorToken = await hre.ethers.getContractFactory("GovernanceToken");
  const token = await governorToken.deploy();

  await token.deployed();

  // console.log(token)
  // let t = await token._afterTokenTransfer()
  // console.log(t)

  console.log(
    `governorToken deployed to ${token.address}`
  );


  const GovernorContract = await hre.ethers.getContractFactory("GovernorContract");
  const contract = await GovernorContract.deploy(token.address, 100, 1, 1, 1);

  await contract.deployed();
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
