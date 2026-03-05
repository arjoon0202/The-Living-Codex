// extract.mjs — Converts a chunk of Codex HTML to clean Markdown
// Usage: node extract.mjs <input.html> <startLine> <endLine> <output.md>

import { readFileSync, writeFileSync } from 'fs';

const [,, inputFile, startLine, endLine, outputFile] = process.argv;
const lines = readFileSync(inputFile, 'utf-8').split('\n');
const chunk = lines.slice(parseInt(startLine) - 1, parseInt(endLine)).join('\n');

let md = chunk
  // Preserve line breaks within paragraphs
  .replace(/<br\s*\/?><br\s*\/?>/gi, '\n\n')
  .replace(/<br\s*\/?>/gi, '  \n')
  // Convert headers
  .replace(/<h2[^>]*class="section-title"[^>]*>(.*?)<\/h2>/gi, '## $1')
  .replace(/<h3[^>]*>(.*?)<\/h3>/gi, '### $1')
  // Convert section labels to small headers
  .replace(/<div[^>]*class="section-label"[^>]*>(.*?)<\/div>/gi, '#### $1')
  // Convert bold and italic
  .replace(/<strong>(.*?)<\/strong>/gi, '**$1**')
  .replace(/<em>(.*?)<\/em>/gi, '*$1*')
  // Convert paragraphs
  .replace(/<p[^>]*class="section-text"[^>]*>/gi, '\n')
  .replace(/<p[^>]*>/gi, '\n')
  .replace(/<\/p>/gi, '\n')
  // Convert move cards (technique cards) to structured sections
  .replace(/<div[^>]*class="move-name"[^>]*>(.*?)<\/div>/gi, '### $1')
  .replace(/<div[^>]*class="move-category"[^>]*>(.*?)<\/div>/gi, '*$1*  ')
  .replace(/<div[^>]*class="move-desc"[^>]*>(.*?)<\/div>/gi, '$1')
  // Convert mission cards
  .replace(/<div[^>]*class="mission-title"[^>]*>(.*?)<\/div>/gi, '### $1')
  .replace(/<div[^>]*class="mission-subtitle"[^>]*>(.*?)<\/div>/gi, '*$1*')
  .replace(/<div[^>]*class="mission-desc"[^>]*>/gi, '\n')
  .replace(/<div[^>]*class="mission-outcome"[^>]*>/gi, '\n**Outcome:** ')
  .replace(/<div[^>]*class="mission-status[^"]*"[^>]*>(.*?)<\/div>/gi, '`$1`  ')
  // Convert comment authors
  .replace(/<div[^>]*class="comment-author[^"]*"[^>]*>(.*?)<\/div>/gi, '\n> **$1:**')
  .replace(/<div[^>]*class="comment-text"[^>]*>(.*?)<\/div>/gi, ' $1')
  // Convert journal entries
  .replace(/<div[^>]*class="journal-date"[^>]*>(.*?)<\/div>/gi, '### $1')
  .replace(/<div[^>]*class="journal-title"[^>]*>(.*?)<\/div>/gi, '## $1')
  .replace(/<div[^>]*class="journal-sig"[^>]*>(.*?)<\/div>/gi, '\n$1\n')
  // Convert tradition/deck cards
  .replace(/<div[^>]*class="tradition-name"[^>]*>(.*?)<\/div>/gi, '### $1')
  .replace(/<div[^>]*class="tradition-desc"[^>]*>/gi, '\n')
  .replace(/<div[^>]*class="deck-room-name"[^>]*>(.*?)<\/div>/gi, '### $1')
  .replace(/<div[^>]*class="deck-room-desc"[^>]*>(.*?)<\/div>/gi, '\n$1\n')
  // Convert companion elements
  .replace(/<div[^>]*class="companion-name[^"]*"[^>]*>(.*?)<\/div>/gi, '# $1')
  .replace(/<div[^>]*class="companion-title-line"[^>]*>(.*?)<\/div>/gi, '*$1*')
  .replace(/<div[^>]*class="companion-bio"[^>]*>/gi, '\n')
  // Convert stat blocks
  .replace(/<div[^>]*class="c-stat-label"[^>]*>(.*?)<\/div>/gi, '**$1:** ')
  .replace(/<div[^>]*class="c-stat-value"[^>]*>(.*?)<\/div>/gi, '$1')
  // Convert protocol cards
  .replace(/<div[^>]*class="protocol-name"[^>]*>(.*?)<\/div>/gi, '### $1')
  .replace(/<div[^>]*class="protocol-designation"[^>]*>(.*?)<\/div>/gi, '*$1*')
  .replace(/<div[^>]*class="protocol-desc"[^>]*>/gi, '\n')
  .replace(/<div[^>]*class="protocol-note"[^>]*>(.*?)<\/div>/gi, '\n> $1\n')
  // Convert ornaments
  .replace(/<div[^>]*class="journal-ornament"[^>]*>.*?<\/div>/gi, '\n---\n')
  // Convert span-based content
  .replace(/<span[^>]*style="[^"]*font-family[^"]*'Noto Sans JP'[^"]*"[^>]*>(.*?)<\/span>/gi, '$1')
  .replace(/<span[^>]*class="[^"]*"[^>]*>(.*?)<\/span>/gi, '$1')
  // Strip remaining HTML tags
  .replace(/<[^>]+>/g, '')
  // Clean up entities
  .replace(/&amp;/g, '&')
  .replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>')
  .replace(/&quot;/g, '"')
  .replace(/&#x27;/g, "'")
  .replace(/&nbsp;/g, ' ')
  .replace(/&#8212;/g, '—')
  .replace(/&#8211;/g, '–')
  .replace(/&#x20BF;/g, '₿')
  // Clean excessive whitespace but preserve intentional double newlines
  .replace(/\n{4,}/g, '\n\n\n')
  .replace(/[ \t]+$/gm, '')
  .trim();

writeFileSync(outputFile, md, 'utf-8');
console.log(`Extracted L${startLine}–L${endLine} → ${outputFile} (${md.split('\n').length} lines)`);
