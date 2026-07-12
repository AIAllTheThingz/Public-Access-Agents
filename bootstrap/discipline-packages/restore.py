#!/usr/bin/env python3
"""Restore the remaining discipline generator sources from verified text chunks."""
from pathlib import Path
import base64
import hashlib
import tarfile

PARTS = [
    ("source.part01.b64", 2000, "9f15396b2522904bf7bd69b5d57584d4f10b165878bb170a4a93e4cb63735251"),
    ("source.part02.b64", 2000, "a6730692eef73b2d97a3eb826c7f2fef80d36061b292eb6406041dc925794ee3"),
    ("source.part03.b64", 2000, "dc3f78832bd68a0e50a2718804117ad79a8b6e8011cc1d073c819cfe0b414b81"),
    ("source.part04.b64", 2000, "677706ff20e68ade29e1c42857a1afb344436281d344d8629a180841b07b36e4"),
    ("source.part05.b64", 2000, "774a14252350e799bf64a3f3f16adaee8c03fe34189e1f9464fd477108a2abcf"),
    ("source.part06.b64", 2000, "64ef01554d8234d406d4daf7e28086f00f668a5e88a69bca9151e6f94a13dde5"),
    ("source.part07.b64", 2000, "650e55b34640a33c7c53908bfffc55db9f81b9fc73817c802ba01a5d8b1f0bb8"),
    ("source.part08.b64", 2000, "41b73030666c2b0e4e31740a57cfe18648d921923afecd0a46557e2ec27a49ef"),
    ("source.part09.b64", 2000, "56dc2f011a7d204c04efeea94a66800a6ae7b0e069124221e43a07d29e2f17ee"),
    ("source.part10a.b64", 500, "19ca2295d4cbefb82a994dbe4d4ed5d016a0e8303d16c39757330be5bd6ba8a5"),
    ("source.part10b.b64", 500, "2bbbebff4e980650770e671996aa3dd5cf145c95f08ca6c3b7df30c303ac93e1"),
    ("source.part10c.b64", 500, "f3e05664afa80b525d109d2d62121dc40a89a70f485b1f11cdbb340602c2d54a"),
    ("source.part10d.b64", 500, "ad9508d635d1cc6c32b9736a962208205b558c63af7670fc835dcdd285e9428c"),
    ("source.part11a.b64", 500, "c78f2cbd1621f35e4e7c18bd1f5c06e705a231dc0510da700ffd45caae85885a"),
    ("source.part11b.b64", 500, "086c1553a9b3dd76b2cf8aab4d561a0d47b398fe73dd714ae2d3f446b203559a"),
    ("source.part11c.b64", 500, "034f8c8fd480d15c855d8c6ea3eff962a5097fe760df4c1a1b02974d9da7f5cb"),
    ("source.part11d.b64", 500, "ca33bc052ad587cb6ac51377f79601a3204612c50b960ca2ce68937704011e15"),
    ("source.part12a.b64", 500, "329b7080c367afa45764d7ea1c19aa4668140e99372fab9652ae3effece0cb54"),
    ("source.part12b.b64", 500, "3305dbce2b4ee8dc9a104b6a9ce65e026614423ed16a36bc68366d474f760881"),
    ("source.part12c.b64", 500, "e1cada377f16a7cd0953a77f71b9e2daac4699123469051804dd63a7a741ea8b"),
    ("source.part12d.b64", 500, "246c75b55c87a60b0d3e3b259d2f7151cbe87c9c0089eddeb9838a2dfe4f19a8"),
    ("source.part13a.b64", 500, "4c55ef7676a30c2dfafaaf1224fa6a42bae34a472edcfe5454ff6e11552fde0b"),
    ("source.part13b.b64", 500, "3673e33aee7ee51c7d9079a607dd8a581ee9422aa9ef84f89568d82f8358b94e"),
    ("source.part13c.b64", 500, "db2e61ebbba573e8588010255058f8cc77081e5be155a1087d542d79ed9dc01a"),
    ("source.part13d.b64", 500, "7214a439bdd3fd2b9d9102d30b75924fdc06203fbac749c721a01dfca1fa01f0"),
    ("source.part14a.b64", 500, "bdeac761bf8d7e8209918ac44b68ffcdc847cdc04b1b4ceee6dff56d6bd1038b"),
    ("source.part14b.b64", 500, "bb0d365a2255c4729afc8f78d5ac5489c9f722fb37d9670a7567c902904cf6de"),
    ("source.part14c.b64", 500, "29ed608e32e80a4aea8a6394d68b168f11cc53be48006dc866dd83ffc66e532b"),
    ("source.part14d.b64", 500, "be35815134703f43c07a95c14e8ae70b18e3b995a00c12e5d7a457e7f53055e2"),
    ("source.part15a.b64", 500, "c584af57098a3a3df1cc457af1992064207485d5fd14e2f6c57521a836a18178"),
    ("source.part15b.b64", 500, "d46d24d7317d1e8420e9409cf158d49f681f301c38df87fdcaadd1263edddcb5"),
    ("source.part15c.b64", 500, "c33bccf9fb75bd657f9adb2aaf06628dd8a01999623e45d85701e65514f4e9aa"),
    ("source.part15d.b64", 56, "bf6d198acc0f6363f556721a2ef45e7aea3601fa004e93d8fbf95e5887c083b5"),
]
ROOT = Path(__file__).resolve().parent
encoded = []
for name, expected_length, expected_sha in PARTS:
    path = ROOT / name
    content = path.read_text(encoding="ascii")
    if len(content) != expected_length:
        raise RuntimeError(f"Invalid source chunk length: {name}")
    actual_sha = hashlib.sha256(content.encode("ascii")).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(f"Source chunk checksum mismatch: {name}")
    encoded.append(content)
archive_bytes = base64.b64decode("".join(encoded), validate=True)
expected_archive_sha = "ab84d501da8f55d237ad540a9d99d022e95125c3ed94e48c8b9bd04f9c85099c"
if hashlib.sha256(archive_bytes).hexdigest() != expected_archive_sha:
    raise RuntimeError("Generator source archive checksum mismatch")
archive_path = ROOT / "source.tar.gz"
archive_path.write_bytes(archive_bytes)
with tarfile.open(archive_path, "r:gz") as archive:
    for member in archive.getmembers():
        member_path = Path(member.name)
        if member_path.is_absolute() or ".." in member_path.parts:
            raise RuntimeError(f"Unsafe archive path: {member.name}")
    archive.extractall(ROOT, filter="data")
print("Generator sources restored and verified.")
