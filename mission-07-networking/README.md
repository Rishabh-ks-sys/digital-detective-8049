# Mission 7 — How Computers Communicate

## 1. Task / Objective

Understand basic networking concepts, observe network connectivity and DNS information, and explain what happens when a website opens in a browser.

## 2. Work Completed

### Task 7.1 — Explain Network Concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | A network covering a small area. | Home Wi-Fi network |
| MAN | A network covering a city or large campus. | City-wide university network |
| WAN | A network covering large geographical areas. | Internet |
| DNS | Converts domain names into IP addresses. | Looking up example.com |
| Router | Connects networks and forwards data between them. | Home Wi-Fi router |
| Protocol | A set of rules devices follow to communicate. | HTTP, HTTPS, TCP |
| Packet switching | Divides data into packets that travel across a network. | Sending a webpage request |
| Client-server | A client requests a service and a server provides it. | Browser requesting a webpage |

### Task 7.2 — Observe Network Information

**Connectivity test**

Command used:

`ping -c 4 example.com`

Result:
- 4 packets transmitted.
- 4 packets received.
- 0.0% packet loss.

This shows that my computer successfully reached the example website during the test.

The connectivity test checks whether a computer can reach another device or website over a network and measures the response time.

**DNS lookup**

Command used:

`nslookup example.com`

Result:
- DNS resolver: 8.8.8.8
- DNS port: 53
- Domain queried: example.com
- Two IP addresses were returned.

A DNS lookup displays the DNS resolver information and the IP addresses associated with a domain name.

**Role of DNS:** DNS translates a human-readable website name into an IP address so that the browser can locate the correct server.

### Task 7.3 — What Happens When You Open a Website?

1. The user enters a website address in the browser.
2. The browser checks whether it already knows the website's IP address.
3. If needed, DNS translates the domain name into an IP address.
4. The client sends a request to the server using a communication protocol such as HTTPS.
5. Routers forward data packets across networks until they reach the server.
6. The server processes the request and sends a response. The browser receives the response and displays the webpage.

## 3. Commands / Tools Used

- `ping -c 4 example.com` — tests network connectivity.
- `nslookup example.com` — performs a DNS lookup.
- Terminal — used to execute network commands.

## 4. My Understanding

A computer network allows devices to communicate and exchange information. DNS helps browsers find servers using domain names. Routers forward data between networks, while protocols define the rules of communication. Client-server communication allows browsers to request webpages from servers.

## 5. Difficulties Faced

No major difficulties were encountered while performing the connectivity test and DNS lookup.

## 6. How I Resolved Them

I used the Terminal commands provided in the assignment and interpreted their outputs to understand connectivity and DNS resolution.

## 7. Evidence / Files

- This README file.
- Connectivity test output from `ping`.
- DNS lookup output from `nslookup`.

Note: Private network information has not been included.

## 8. Commit Details

Networking concepts and website communication.

