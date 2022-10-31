describe('empty spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:31001/')
    cy.get('#hello')
    .should('have.text', 'Helloooo Test World!')
  })
})