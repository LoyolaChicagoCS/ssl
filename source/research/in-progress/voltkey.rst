:orphan:

`Voltkey <https://neilklingensmith.com/research.php>`_
======================================================

The goal of VoltKey is to make deployment and maintenance of new IoT devices easy. Currently, when we install new IoT devices, we need to go through a complex process of connecting the device to the WiFi network. With VoltKey, no configuration is necessary: you just plug the new device in and it works.

VoltKey is a plug that generates USB power for IoT devices from a 120V wall outlet. It harvests entropy (noise) from the wall power and generates a unique security key that the IoT device can use to authenticate to the local WiFi network.

The main areas of focus for VoltKey are Context-Based Authentication (CBA) and applied Internet of Things (IoT). Voltkey has several branches of work that stem from the project. Moonshine is one of those projects; Moonshine is a randomness distiller for abstract noise sources for compact IoT devices. We were able to apply methods gathered from Voltkey to a new space and make improvements in randomness distillation. Voltkey explores the applicability of new algorithmic methods to generate and filter keys to be more random and more secure.

Video Demonstration:
--------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/SIn331PUXlM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  

Team Members
------------------

- |Neil Klingensmith|
- |George K. Thiruvathukal|
- Jack West

Key Publications
------------------

- Kyuin Lee, Neil Klingensmith, Younghyun Kim, Suman Banerjee, *VoltKey: Continuous Secret Key Generation based on Power Line Noise for Zero-Involvement Pairing and Authentication*, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT), September 2019
- Kyuin Lee, Neil Klingensmith, Dong He, Suman Banerjee, and Younghyun Kim. 2020. IvPair: context-based fast intra-vehicle device pairing for secure wireless connectivity. In Proceedings of the 13th ACM Conference on Security and Privacy in Wireless and Mobile Networks (WiSec '20). Association for Computing Machinery, New York, NY, USA, 25–30.
- West, J., VoNguyen, T., Ahlgren, I., Motyashok, I., Thiruvathukal, G. K., Klingensmith, N., ... & Banerjee, S. Demo Abstract: VoltKey: Using Power Line Noise for Zero–Involvement Pairing and Authentication.