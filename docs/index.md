# Making KeyChain better
Our goal is to improve the Apple ecosystem experience
1. Making faster, simpler, and easier for users to sign in to websites and apps using KeyChain
2. Increase user security

We'll breakdown what this tool can do, how, and by focusing on its users pain points, we'll design an alternative UI that would make KeyChain the trustworthy, reliable app that it should be.


## What is KeyChain
Apple users don't understand what is or how to use KeyChain. Don't believe me? Ask the Mac user sitting next to you how to look up the password that they're using to connect to a WiFi.

KeyChain is Apple's secrets management system. Keychain stores users' passwords, authentication credentials, and other sensitive information in either on their iCloud account or on their MacOS device.

• KeyChain offers API for developers to encrypt and store important secrets & information directly in his iCloud account (the iCloud Keychain) that can be reused at next visits (such as a password)

• KeyChain allows users to secure light text format notes with your system (iCloud) password — at this time, they can exclusively be added from within the Keychain app

• KeyChain allows users to view private keys created — To be researched how it works

• Keychain allows users to manage, edit or add system certificate to protect the MacOS or iOS user. Most users never touch this feature

• Keychain allow users to setup additional KeyChain with new security settings, such as a new password and it can be locked

• Keychain allows external apps to ensure they are the only ones with access to a password

• Keychain ensures data encryption before storage

## User stories


## What are the problems with Keychain?
1. Keychain don't auto-fill passwords for all websites
2. Keychain does not auto-fill passwords for all iOS app
3. Sign up or Reset Password fields don't update
4. When no paswords are suggested, the current feature does not allow a manual password creation
5. It's unclear on MacOS if the password is stored locally or on iCloud
6. Novice users have to choose between local storage and iCloud and it is confusing to them
7. On the MacOs
8. Making iCloud visible sometimes require a user to disabling iCloud Keychain and re-enabling it

## To-do
- [] Add user stories (various devices, scenarios, etc.)
- [] Research how Keys are added to KeyChain
- [] Research what ticket viewer is
- [] Research why create new certificate using certificate assistant
