import { defineConfig } from "tinacms";

/* TinaCMS scaffold for the Brilliantly Sane journal.
   Not wired up yet. To finish it:
     1. npx @tinacms/cli@latest init   (creates the app shell and .env)
     2. add TINA_CLIENT_ID and TINA_TOKEN from tina.io
     3. npx tinacms dev -c "python3 tools/content.py"
   Posts live in content/journal/*.md and are the source of truth.
   After Lisa edits a post, tools/content.py regenerates journal/<slug>/index.html. */

export default defineConfig({
  branch: process.env.GITHUB_BRANCH || "main",
  clientId: process.env.TINA_CLIENT_ID || "",
  token: process.env.TINA_TOKEN || "",
  build: { outputFolder: "admin", publicFolder: "." },
  media: { tina: { mediaRoot: "assets/img", publicFolder: "." } },
  schema: {
    collections: [
      {
        name: "post",
        label: "Journal posts",
        path: "content/journal",
        format: "md",
        ui: {
          router: ({ document }) => `/journal/${document._sys.filename}/`,
        },
        fields: [
          { type: "string", name: "title", label: "Title", isTitle: true, required: true },
          { type: "datetime", name: "date", label: "Date", required: true },
          { type: "string", name: "readingTime", label: "Reading time", description: 'Shown next to the date, for example "4 min".' },
          { type: "string", name: "excerpt", label: "Excerpt", ui: { component: "textarea" },
            description: "One or two sentences. Used on the journal index and as the meta description." },
          { type: "boolean", name: "draft", label: "Draft", description: "Drafts are skipped by the build." },
          { type: "rich-text", name: "body", label: "Body", isBody: true },
        ],
      },
    ],
  },
});
