Title: Server consolidation, migration, and simplification
Date: 2025-04-14
Category: Tech Musings

Like most people who love to tinker, I have several self-hosted services I run. And I had those services sprinkled across several different devices. I had a Raspberry Pi 2B, a custom built gaming desktop, and a VPS hosted on [Linode](https://www.linode.com/).

The Raspberry Pi was my [Syncthing](https://syncthing.net/) always on device, for the rest of the nodes in the cluster to have available to use. I was running Raspberry Pi OS Bullseye on that. I've had that since early 2016, always doing _something_.

My Linode VPS was running an OpenVPN server and a personal blog using [Ghost](https://ghost.org/). I also had a [little Python program I wrote](https://github.com/ghuitster/secret-santa) to help my family with secret Santa name selection every year. It was running Ubuntu Server 24.04. I've had that server since July 2017. I was really pleased with Linode. Their pricing is good, the server performed well, and their management site is good. I used Linode for my name servers as well and it was a positive experience. Anyone looking for a cloud VPS hosting provider, I would give Linode a look.

My custom built gaming desktop is a rig I made in March 2023. It runs Windows 11 Pro. This was my heavy hitter running Plex Media Server and Backblaze personal backup. Our Plex media consists of content we've ripped from disks we own (they're all in boxes in the basement now). We have our music, and our personal photos/videos on it. In total, our Plex library is about 11 TB of stuff.

On a whim I measured the power usage of my desktop using my Kill-A-Watt. At idle, that computer was using about 114 watts, for a yearly total of almost exactly one MEGA WATT HOUR. According to our whole-home solar/battery solution, that was 9.3% of the power our entire house used in 2024. That is insane to me. So I decided it was time to make some changes! It was time to centralize everything, pick better solutions, and decrease my power usage.

I started all of my research on this venture by reading lots of stuff. [This](https://github.com/zilexa/Homeserver/blob/master/Recommendations.md) guide in particular was very helpful and concise for hardware recommendations. My first idea was to build something using the ASrock DeskMini 310 as a starter. I'm not really sure what changed my mind, but that's not what I ended up doing. I ended up with a used Intel NUC I picked up on the cheap from Ebay. I was pretty sure I wanted to keep using Backblaze for my offsite backup, and Backblaze personal has great pricing for what we do. Which meant I was going to have to use Windows. I knew I wanted Windows 11, so that meant I was looking at 8th gen Intel or newer. Which is perfect, because that met my needs for Plex hardware transcode using Intel Quick Sync.

I ended up buying a [Cenmate HDD enclosure](https://www.amazon.com/dp/B0DD3H6ZVS) to be a Direct Attached Storage device. So far, that has worked really well. I have three drives in it and they stay below 46 degrees C. It's plenty fast for three 5400 RPM HDDs.

My blog is now built using [Pelican](https://getpelican.com/), a static site generator built using Python. I have an Ubuntu laptop with Python already installed so that was a perfect solution for me. I'm using [static-web-server](https://github.com/static-web-server/static-web-server) to host the site. I'm honestly quite impressed with this setup. It's a lot fewer parts/pieces than my previous solution and it's faster too. The http to https redirect was a lot easier than my previous hand rolled Nginx config.

I decided to use WireGuard instead of OpenVPN. To get up and running I used [WgServerForWindows](https://github.com/micahmo/WgServerforWindows), which made it really easy to get up and rolling. I really like the speed WireGuard offers, and the increased security over OpenVPN. Also, it's awesome to have a VPN to my home network that I can connect to and get into my stuff at home. I've already connected a bunch of times and it's reliable and speedy.

I have grown up a bunch with my server management skills so I decided to go with Porkbun for my DNS registrar and CloudFlare for my nameservers. I know CloudFlare can do it all, but I was nervous about giving CloudFlare my credit card because I think it's easy to accidentally spend a bunch of money on them. This way, they don't even have my credit card info so I can't spend any money there. Setting up DNS was straight forward between them. I finally have DNSSEC capabilities (my prior hosting DNS/NS setup didn't have that capability). I love CloudFlare's Origin Server capability, so that's what static-web-server is using. For Dynamic DNS I have a [DnsTube](https://github.com/drittich/DnsTube) service running on my NUC with a CloudFlare API key.

Syncthing was easy to install on the NUC. And as a bonus, I finally decided to install it on our phones so family photos and videos sync nightly to the NUC for backup to Backblaze as well.

Plex was a straight-forward migration from the desktop. I've been running Plex for several years already so that was easy. I did have to disable HDR to SDR tone mapping, and disable HDR to HDR transcoding. If I kept that enabled, it would play a black screen with audio. So if you want to watch 4K you can either direct stream it or transcode to some flavor of 1080p.

Backblaze was also an easy install. I started with a fresh backup to make it clear this was a new computer. It's chugging through my stuff uploading everything at about 1.3 TB/day.

As an added bonus, I decided to redo the cable routing in the office. I even busted out my ethernet cable terminator and made some super short cables for the two wireless printers. Much less cable mess, and now everything in the office is hooked up to my UPS! Oh, yeah I also installed a piece of software on the NUC so it'll safely shut after being on UPS power for a few minutes.

I also set up a backup from the desktop to the NUC, which I accomplished using a startup Windows scheduled task on the desktop with RoboCopy. I am seriously impressed with how fast RoboCopy is. After the initial backup is done, it is able to check that everything is in sync in just a few seconds.

So how did I do?

- I'm down to one server to manage
- My idle consumption between NUC and HDD enclosure is 28 watts (!!!)
	- NUC consumes 4.3 watts at idle
	- HDD enclosure is the remaining 23.7 watts
	- Yearly consumption 1 MWh -> 245 kWh
- Saving $5/month no longer paying for Linode

Things I don't love

- I miss having a Linux server
	- I very well might go back to Linux at some point and find a new backup solution
	- For now, I'm happy with what I have
- The fan in the Cenmate enclosure is a bit loud
	- I might do some custom 3d printing stuff to make a custom shroud and swap out for a 120 mm Noctua fan