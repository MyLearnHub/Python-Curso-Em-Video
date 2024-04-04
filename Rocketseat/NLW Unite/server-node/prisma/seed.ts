import { prisma } from "../src/lib/prisma";

async function seed() {
  await prisma.event.create({
    data: {
      id: "308698db-a662-4de7-9946-3650bf9cbeae",
      title: "Unite Summit",
      slug: "unite-summit",
      details: "Um evento p/ devs apaixonados por código!",
      maximumAttendees: 120,
    },
  });
}

seed().then(() => {
  console.log("Database seeded!");
  prisma.$disconnect();
});
